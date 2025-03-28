from django.db import models

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    path = models.FileField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
