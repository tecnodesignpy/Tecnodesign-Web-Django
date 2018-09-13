from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre	 			= models.CharField(max_length=100, blank='true', null='true')
    email	 			= models.CharField(max_length=100, blank='true', null='true')
    mensaje	 			= models.CharField(max_length=2000, blank='true', null='true')
    ip	 				= models.CharField(max_length=100, blank='true', null='true')
    fecha_creado	 	= models.DateTimeField(auto_now_add=True)