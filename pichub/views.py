# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the pichub')

def image(request):
    image = Image.objects.all()
    return render(request, 'pic.html', {"image" : image})    
