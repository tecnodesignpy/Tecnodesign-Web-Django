from django.contrib import admin
from .models import *
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'online','logo','fecha_creado',
    )    

def _register(model, admin_class):
    admin.site.register(model, admin_class)
	
	
_register(Cliente,ClienteAdmin)