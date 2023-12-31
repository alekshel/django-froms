from django.db import models

from groups.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    groups = models.ManyToManyField(Group, related_name="students", blank=True)

    def __str__(self):
        return f"ID: {self.pk} {self.first_name}"
