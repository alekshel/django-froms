from django.db import models


class Subject(models.Model):
    name = models.CharField("Назва предмету", max_length=100, default="")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField("ПІБ", max_length=255, default="")
    birth_date = models.DateField("Дата народження", default="")
    subjects = models.ForeignKey(
        Subject, verbose_name="Предмети", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
