from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def databasetable(request):
    TOB=Topic.objects.all()
    TOB=Topic.objects.all()[:2:]
    TOB=Topic.objects.all().order_by('topic_name')
    TOB=Topic.objects.all().order_by('-topic_name')
    TOB=Topic.objects.all().order_by(Length('topic_name'))
    TOB=Topic.objects.all().order_by(Length('topic_name').desc())
    d={'table':TOB}
    return render(request,'databasetable.html',d)



def webtable(request):
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'webtable.html',d)

def displaylocation(request):
    LOLO=Location.objects.all()
    LOLO=Location.objects.filter(age__gt=22)
    LOLO=Location.objects.filter(age__gte=25)
    LOLO=Location.objects.filter(age__lt=25)
    LOLO=Location.objects.filter(age__lte=25)

    d={'name':LOLO}
    return render(request,'displaylocation.html',d)
