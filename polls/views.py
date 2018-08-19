# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Imagen

# Create your views here.
def index(request):
    lista_imagenes = Imagen.objects.all()
    context = {'lista_imagenes': lista_imagenes}
    return render(request, 'polls/index.html', context)