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


class DocumentAPIView(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated,]


class DocumentDetailAPIView(ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, ]


class DocumentUploadViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticatedOrReadOnly, ]

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

        serializer = self.get_serializer(data={'file_name': file_obj.name, 'text': text})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DocumentSearchAPIView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = DocumentFilter
    ordering_fields = ['file_name', 'created_at']
    ordering = ['-created_at']