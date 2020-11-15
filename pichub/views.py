# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Category


# Create your views here.
def image(request):
    image = Image.objects.all()
    return render(request, 'pic.html', {'image': image})


def search_results(request):
    if 'searchimage' in request.GET and request.GET["searchimage"]:
        category = request.GET.get("searchimage")
        searched_images = Image(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "Sorry! You haven't searched for any image"
        return render(request, 'search.html', {"message": message})        
