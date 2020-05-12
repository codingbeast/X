from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import xml.etree.ElementTree as ET
from alfa import helper,crypto
import os
import json
from alfa.serializer import VideosSerializer
from .models import details
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
import requests
# Create your views here.
def myupdate(request):
    status=helper.dbdelete()
    a=helper.xmlfiles()[2]
    tree = ET.parse(a)
    videos=tree.findall("Video")
    for video in videos:
        title=video.find("Title").text
        Image=video.find("Image").text
        Url=video.find("Url").text
        tag=video.find("tag").text
        videotype=video.find("videotype").text
        a={
            "title" : title,
            "image" : Image,
            "Url" : Url,
            "tag" : tag,
            "videoType" : videotype,
        }
        helper.dbinsert(mydict=a)

    return JsonResponse(a,safe=False)
def allcategories(request):
    a=helper.GetAllCategories()
    return JsonResponse(list(a),safe=False)
@api_view(('GET',))
def mylist(request):
    paginator = PageNumberPagination()
    paginator.page_size = 9
    mydata= details.objects.all()
    context = paginator.paginate_queryset(mydata, request)
    serializer = VideosSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)
def homepage(request):
    if request.method == "GET":
        try:
            page_number = request.GET['page']
        except:
            page_number=1
    context=helper.pagination_logic(page_number)
    return render(request,"index.html",context)
def watch(request):
    if request.method == "GET":
        urlid=request.GET['id']
        url=crypto.decrypt(urlid)
        data=details.objects.get(url=url)
        context={
            "my" : data
        }

    return render(request,"watch.html",context)