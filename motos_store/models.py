from django.db import models

# Create your models here.
class Moto(models.Model):
    color = models.CharField(max_length=255)
    price= models.FloatField()
    state = models.CharField(max_length=255)
    displacement = models.IntegerField()
    model = models.CharField(max_length=255)
    image_url = models. URLField(max_length=255, blank=True, null=True)

class Marca(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class moto_marca(models.Model):
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
