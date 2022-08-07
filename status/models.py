from django.db import models

# Create your models here.
class Status(models.Model):
    content = models.TextField(max_length=255, blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True, null=True)