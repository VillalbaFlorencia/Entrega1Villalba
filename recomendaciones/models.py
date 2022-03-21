from django.db import models

class Series(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()
    
    def __str__(self):
        return f'{self.nombre}'
 
    
class Peliculas(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()
    
    def __str__(self):
        return f'{self.nombre}'
    
    
class Documentales(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    netflix = models.BooleanField()

    def __str__(self):
        return f'{self.nombre}'