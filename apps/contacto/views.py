from django.shortcuts import render
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import JsonResponse
import json
from django.core import serializers
# Create your views here.
# Importamos los modelos Clientes y Portfolio
from apps.clientes.models import *
from apps.portfolio.models import *
#
from django.db.models.aggregates import Count
from django.db.models import Max
from random import randint
import random
#
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def send_email(request):
    if request.method == "POST":
        print("entro")
        v_nombre 	= request.POST.get('nombre')
        v_email	 	= request.POST.get('email')
        v_mensaje 	= request.POST.get('mensaje')
        contacto 	= Contacto(nombre= v_nombre, email= v_email, mensaje= v_mensaje, ip= 0)
        contacto.save()

        html_content = "Nombre: "+v_nombre+" <br>Email: "+v_email+" <br>Mensaje: "+v_mensaje
        send_mail("Nuevo Contacto en la Web","","noreply@tecnodesign.com.py", ['ledezmatto@tecnodesign.com.py'],
            html_message=html_content)

        data = [contacto]
    else:
        print("no entro")
        data = []
    return JsonResponse(serializers.serialize('json', data), safe= False)



def website(request):
    portfolio       = sorted(Portfolio.objects.filter(online=True), key=lambda x: random.random())
    clientes        = Cliente.objects.filter(online=True)
    galeria        = Galeria.objects.all()
    return render(request,'index.html',{'clientes':clientes,'portfolio':portfolio,'galeria':galeria})

def error404(request):
    clientes        = sorted(Cliente.objects.filter(online=True), key=lambda x: random.random())
    return render(request,'404.html',{'clientes':clientes})



    












