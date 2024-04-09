# Generated by Django 5.0.3 on 2024-04-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("business_certificate", models.FileField(upload_to="certificates/")),
                (
                    "business_logo",
                    models.ImageField(blank=True, null=True, upload_to="logos/"),
                ),
                ("owner_first_name", models.CharField(max_length=100)),
                ("owner_last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
                ("preferred_contact_method", models.CharField(max_length=50)),
                ("how_found", models.CharField(max_length=255)),
                (
                    "referred_by",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("recruiting_year", models.CharField(max_length=4)),
                ("source_country", models.CharField(max_length=100)),
                ("services_provided", models.TextField()),
            ],
        ),
    ]