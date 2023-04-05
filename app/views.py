from django.shortcuts import render
from app.models import *

# Create your views here.
def databasetable(request):
    TOB=Topic.objects.all()
    d={'table':TOB}
    return render(request,'databasetable.html',d)



def webtable(request):
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'webtable.html',d)

def displaylocation(request):
    LOLO=Location.objects.all()
    d={'name':LOLO}
    return render(request,'displaylocation.html',d)
