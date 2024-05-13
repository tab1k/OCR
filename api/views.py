from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters
from .filters import DocumentFilter
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .data_extraction import *
import re

class DocumentAPIView(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [AllowAny,]


class DocumentDetailAPIView(ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [AllowAny, ]


class DocumentUploadViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        text = ''
        if file_obj.name.endswith('.pdf'):
            # Обработка PDF-файлов
            pdf_reader = PdfReader(file_obj)
            for page in pdf_reader.pages:
                text += page.extract_text()
        else:
            # Обработка других форматов файлов (например, изображений)
            # Открыть файл изображения
            image = Image.open(file_obj)
            # Используйте pytesseract для извлечения текста из изображения
            text = pytesseract.image_to_string(image)



        # Извлечение данных из текста и сохранение их в соответствующих переменных
        extracted_full_name = extract_full_name(text)
        extracted_position = extract_position(text)
        extracted_birth_info = extract_birth_info(text)
        extracted_citizenship = extract_citizenship(text)
        passport_number = extract_passport_number(text)
        passport_issue_date = extract_passport_issue_date(text)
        issuing_authority = extract_issuing_authority(text)
        iin = extract_iin(text)
        insurance_company_name = extract_insurance_company_name(text)
        extracted_education_institution = extract_education_institution(text)
        extracted_education_period = extract_education_period(text)
        extracted_education_specialty=extract_education_specialty(text)
        extracted_diploma_details = extract_diploma_details(text)

        # Извлеките другие данные, если необходимо

        serializer = self.get_serializer(data={'file_name': file_obj.name, 'text': text})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Создание объекта Document
        document = serializer.instance

        # Создание объекта DocumentData с извлеченными данными
        document_data = DocumentData.objects.create(
            document=document,
            full_name=extracted_full_name,
            position=extracted_position,
            date_and_place_of_birth=extracted_birth_info,
            citizenship=extracted_citizenship,
            passport_number=passport_number,
            passport_issue_date=passport_issue_date,
            issuing_authority=issuing_authority,
            iin=iin,
            insurance_company_name=insurance_company_name,
            education_institution=extracted_education_institution,
            education_period=extracted_education_period,
            education_specialty=extracted_education_specialty,
            education_diploma_details=extracted_diploma_details,

        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class DocumentSearchAPIView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = DocumentFilter
    ordering_fields = ['file_name', 'created_at']
    ordering = ['-created_at']