from django.db import models

# Create your models here.

class Finch(models.Model):
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()


#changing this instance metod doesn't impact the database,
#therefore no makemigration needed
    def __str__(self):
        return f'{self.name} ({self.id})'