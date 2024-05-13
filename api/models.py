from django.db import models


class Document(models.Model):
    file_name = models.CharField(max_length=100, blank=False, null=False)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class DocumentData(models.Model):
    document = models.OneToOneField('Document', on_delete=models.CASCADE, related_name='document_data')
    created_at = models.DateTimeField(auto_now_add=True)

    # Общие сведения
    full_name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True)

    # Общие сведения
    date_and_place_of_birth = models.CharField(max_length=100, blank=True, null=True)  # Дата и место рождения
    citizenship = models.CharField(max_length=100, blank=True, null=True)  # Гражданство
    passport_number = models.CharField(max_length=50, blank=True, null=True)  # Номер паспорта
    passport_issue_date = models.DateField(blank=True, null=True)  # Дата выдачи паспорта
    issuing_authority = models.CharField(max_length=100, blank=True, null=True)  # Орган, выдавший паспорт
    iin = models.CharField(max_length=12, null=True, blank=True)  # ИИН (Индивидуальный Идентификационный Номер)
    insurance_company_name = models.CharField(max_length=200, blank=True, null=True)  # Наименование страховой организации

    # Образование
    education_institution = models.CharField(max_length=255, null=True)
    education_period = models.CharField(max_length=255, null=True)
    education_specialty = models.CharField(max_length=255, null=True)
    education_diploma_details = models.CharField(max_length=255, null=True)

    # Сведения о супруге и родственниках
    spouse_name = models.CharField(max_length=255, null=True)
    spouse_birth_year = models.IntegerField(null=True)
    spouse_occupation = models.CharField(max_length=255, null=True)

    # Сведения о юридических лицах
    legal_entity_name = models.CharField(max_length=255, null=True)
    legal_entity_activity = models.CharField(max_length=255, null=True)
    legal_entity_share_percentage = models.FloatField(null=True)

    # Сведения о трудовой деятельности
    employment_period = models.CharField(max_length=255, null=True)
    employment_organization = models.CharField(max_length=255, null=True)
    employment_position = models.CharField(max_length=255, null=True)
    employment_disciplinary_actions = models.BooleanField(default=False)
    employment_termination_reason = models.CharField(max_length=255, null=True)

    # Сведения об аудите
    audit_organization = models.CharField(max_length=255, null=True)
    audit_year = models.IntegerField(null=True)
    audit_financial_report = models.CharField(max_length=255, null=True)

    # Сведения о членстве в инвестиционных комитетах
    investment_committee_period = models.CharField(max_length=255, null=True)
    investment_committee_organization = models.CharField(max_length=255, null=True)

    # Судебные разбирательства
    legal_proceedings_involved = models.BooleanField(default=False)
    legal_proceedings_date = models.DateField(null=True, blank=True)
    legal_proceedings_organization = models.CharField(max_length=255, null=True, blank=True)
    legal_proceedings_issue = models.TextField(null=True, blank=True)
    legal_proceedings_decision = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Данные извлечены из {self.document.file_name}"

    class Meta:
        verbose_name = "Обработанный документ"
        verbose_name_plural = "Обработанные документы"
