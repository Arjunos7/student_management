from django.db import models

class Students(models.Model):
    student_number=models.PositiveIntegerField()
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    field_to_study=models.CharField(max_length=200)
    percentage=models.FloatField()

    def __str__(self):
        return f'Students:{self.first_name} {self.last_name}'
