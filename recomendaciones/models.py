from django.db import models
from ckeditor.fields import RichTextField

class Series(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()
    descripcion = models.CharField(max_length=50, null = True)
    
    def __str__(self):
        return f'{self.nombre}, {self.categoria}'
 
    
class Peliculas(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()
    
    def __str__(self):
        return f'{self.nombre}, {self.categoria}'
    
    
class Documentales(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()

    def __str__(self):
        return f'{self.nombre}, {self.categoria}'