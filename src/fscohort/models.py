from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"
