from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

FILTROS = ((1, 'Apps'),
           (2, 'Websites'),
           (3, 'Branding'),
           (4, 'SocialMedia'),
           (5, 'Software'))


class Portfolio(models.Model):
    empresa 			= models.CharField(max_length=200, blank='true', null='true')
    titulo 				= models.CharField(max_length=2000, blank='true', null='true')
    tags				  = MultiSelectField(choices=FILTROS, max_choices=3, blank=True, null=True, default='')
    online 				= models.BooleanField(default=False)
    portada				= models.ImageField(default='', blank=True, null=True, upload_to='portfolio/portada')
    fecha_creado	= models.DateTimeField(auto_now_add=True)

    def __unicode__(self,):
        return str(self.empresa)


def change_galeria_name(instance, filename):
    """
    Returns the upload path for the someapp media files, which is in a
    separate folder for clarity and also separated for each tenants.
    """
    return "%s/%s/%s/%s" % ('portfolio','galeria',instance.portfolio.empresa,filename)

class Galeria(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=change_galeria_name)

    def __unicode__(self,):
        return str(self.portfolio)