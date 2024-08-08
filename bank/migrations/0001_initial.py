# Generated by Django 4.1 on 2024-03-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="customers",
            fields=[
                (
                    "Aadhar_number",
                    models.IntegerField(primary_key="True", serialize=False),
                ),
                ("Account_no", models.IntegerField()),
                ("Customer_name", models.CharField(max_length=20)),
                ("Balance", models.IntegerField()),
                ("Date_of_opening", models.DateField()),
            ],
        ),
    ]
