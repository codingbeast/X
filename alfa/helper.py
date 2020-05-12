from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
from alfa import helper,crypto
import xml.dom.minidom
from X import settings
import os
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import details
import requests
def xmlfiles(mylocation="xml"):
    s = StaticFilesStorage()
    xmls=list(get_files(s, location=mylocation))
    xmlfiles=[(os.path.join(settings.STATIC_ROOT,filename)) for filename in xmls]
    return xmlfiles
def dbinsert(mydict):
    myinst=details()
    myinst.title = mydict['title']
    myinst.image = mydict['image']
    myinst.url = mydict['Url']
    myinst.tag = mydict['tag']
    myinst.videotype = mydict['videoType']
    try:
        myinst.save()
        return True
    except:
        return False
def dbdelete():
    try:
        details.objects.all().delete()
        return True
    except:
        return False
def GetAllCategories():
    categories=details.objects.values('tag')
    return categories
def pagination_logic(page_number):
    baseurl="http://localhost:8000/list/?page={0}".format(page_number)
    response=requests.get(baseurl)
    serialdata=json.loads(response.text)
    try:
        nextpage="?"+serialdata['next'].split("?")[-1]
    except:
        nextpage="#"
    try:
        previewpage="?"+serialdata['previous'].split("?")[-1]
        if "page" not in  previewpage:
            previewpage="?page=1"
    except:
        previewpage="#"
    data=serialdata['results']
    for d in data:
        Myurl=d["url"]
        encurl=crypto.encrypt(Myurl)
        d["url"]=encurl
    context={
        "nextpage" : nextpage,
        "previewpage" : previewpage,
        "data" : data,
    }
    return context