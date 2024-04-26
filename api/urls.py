from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'view', DocumentAPIView, basename='document')
router.register(r'view/detail', DocumentDetailAPIView, basename='document-detail')
router.register(r'upload', DocumentUploadViewSet, basename='document-upload')


urlpatterns = [
    path('api/', include((router.urls, 'api'))),
    path('api/search/', DocumentSearchAPIView.as_view(), name='document-search'),
]
