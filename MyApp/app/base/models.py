from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.TextField(max_length=150)
    title = models.TextField(max_length=150)
    description = models.TextField(max_length=900)
    content = models.TextField(max_length=900000)

    def __str__(self):
        return self.name