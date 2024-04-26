import django_filters
from .models import Document


class DocumentFilter(django_filters.FilterSet):
    file_name = django_filters.CharFilter(lookup_expr='icontains')
    text = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Document
        fields = ['file_name', 'text', 'created_at']
