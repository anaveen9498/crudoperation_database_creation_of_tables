from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
from django.http import HttpResponse

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
    LOW=Webpage.objects.filter(player_name__startswith='n')
    LOW=Webpage.objects.filter(player_name__endswith='u')
    LOW=Webpage.objects.filter(player_name__contains='a')
    LOW=Webpage.objects.filter(player_name__in=('Naveen','DilliBabu'))
    LOW=Webpage.objects.filter(player_name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(topic_name='vollyboll') & Q(player_name='Naveen'))
    LOW=Webpage.objects.filter(Q(topic_name='Hocky'))
    LOW=Webpage.objects.all()


    d={'web':LOW}
    return render(request,'webtable.html',d)

def displaylocation(request):
    LOLO=Location.objects.all()
    LOLO=Location.objects.filter(age__gt=22)
    LOLO=Location.objects.filter(age__gte=25)
    LOLO=Location.objects.filter(age__lt=25)
    LOLO=Location.objects.filter(age__lte=25)
    LOLO=Location.objects.filter(Date__year__gt='2022')
    LOLO=Location.objects.filter(Date__year='2023')
    LOLO=Location.objects.filter(Date__day__gt='05')


    d={'name':LOLO}
    return render(request,'displaylocation.html',d)




def display_update(request):
    Webpage.objects.filter(player_name='DilliBabu').update(Email='rolex@gmail.com')
    Webpage.objects.filter(player_name='Naveen').update(topic_name='Hocky')


    TO=Topic.objects.get(topic_name='Kabadi')
    TO.save()
    T=Topic.objects.get(topic_name='Chess')
    T.save()
    Webpage.objects.update_or_create(player_name='Karthik',defaults={'topic_name':TO})
    Webpage.objects.update_or_create(player_name='Karthik',defaults={'Email':'karthikarthikar@gmail.com'})
    Webpage.objects.update_or_create(player_name='DSP',defaults={'topic_name':T,'url':'http://dspdsp.in','Email':'Devichar143@gmail.com'})[0]
    
    d={'web':Webpage.objects.all()}

    return render(request,'webtable.html',context=d)



def display_delete(request):


    Webpage.objects.filter(player_name='Naveen').delete()
    Webpage.objects.filter(player_name__in=('Karthik','DSP')).delete()

    d={'web':Webpage.objects.all()}


    return render(request,'webtable.html',d)
