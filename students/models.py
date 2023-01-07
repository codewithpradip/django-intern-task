from django.db import models
from uuid import uuid4

# Create your models here.
class Students(models.Model):
    id = models.URLField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    grade = models.CharField(max_length=2)
    major = models.CharField(max_length=100)

    def __str__(self):
        return f'Student: {self.name} {self.major}'