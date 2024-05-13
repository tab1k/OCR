# Generated by Django 5.0.4 on 2024-05-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document",
            name="text",
        ),
        migrations.AddField(
            model_name="document",
            name="audit_financial_report",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="audit_organization",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="audit_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="education_diploma_details",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="education_institution",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="education_specialty",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="employment_disciplinary_actions",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="document",
            name="employment_organization",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="employment_period",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="employment_position",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="employment_termination_reason",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="full_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="investment_committee_organization",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="investment_committee_period",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_entity_activity",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_entity_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_entity_share_percentage",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_proceedings_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_proceedings_decision",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_proceedings_involved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_proceedings_issue",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="legal_proceedings_organization",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="position",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="spouse_birth_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="spouse_name",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="document",
            name="spouse_occupation",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
