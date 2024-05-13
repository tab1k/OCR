# Generated by Django 5.0.4 on 2024-05-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_documentdata"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="documentdata",
            options={
                "verbose_name": "Обработанный документ",
                "verbose_name_plural": "Обработанные документы",
            },
        ),
        migrations.AddField(
            model_name="documentdata",
            name="citizenship",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="documentdata",
            name="date_and_place_of_birth",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="documentdata",
            name="iin",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name="documentdata",
            name="insurance_company_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="documentdata",
            name="issuing_authority",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="documentdata",
            name="passport_issue_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="documentdata",
            name="passport_number",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
