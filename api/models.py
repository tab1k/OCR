from django.db import models


class Document(models.Model):
    file_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

