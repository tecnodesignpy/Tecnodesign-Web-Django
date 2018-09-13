from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre 				= models.CharField(max_length=200, blank='true', null='true')
    online 				= models.BooleanField(default=False)
    logo				= models.ImageField(default='', blank=True, null=True, upload_to='clientes/logos')
    fecha_creado	 	= models.DateTimeField(auto_now_add=True, auto_now=False)