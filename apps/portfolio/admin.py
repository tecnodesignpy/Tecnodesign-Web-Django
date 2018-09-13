from django.contrib import admin
from .models import *
# Register your models here.


class GaleriaInline(admin.TabularInline):
    model = Galeria
    extra = 4

class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'empresa',
        'titulo','online','portada','fecha_creado',
    )    
    inlines = [ GaleriaInline,]

def _register(model, admin_class):
    admin.site.register(model, admin_class)
	
	
_register(Portfolio,PortfolioAdmin)