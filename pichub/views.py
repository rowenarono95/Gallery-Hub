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
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'pic/search.html', {"message": message, "images": searched_images})
    else:
        message = "Sorry! You haven't searched for any image"
        return render(request, 'pic/search_results.html', {"message": message})        
