# Generated by Django 4.2.6 on 2023-10-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0004_alter_student_groups"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=15, null=True),
        ),
    ]