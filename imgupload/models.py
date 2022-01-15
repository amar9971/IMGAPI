from django.db import models

# Create your models here.
from django.db import models


class Profile(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['image', str(instance.name), filename])

    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=nameFile, blank=True)
