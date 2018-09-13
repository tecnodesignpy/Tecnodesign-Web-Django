from django.contrib import admin
from .models import *
# Register your models here.


class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'email','mensaje','ip','fecha_creado'
    )    

def _register(model, admin_class):
    admin.site.register(model, admin_class)
	
	
_register(Contacto,ContactoAdmin)