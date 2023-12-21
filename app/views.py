from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get(topic_name=tn)
    n=input('enter name: ')
    u=input('enter url: ')
    e=input('enter email: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    WO.save()
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    pk=int(input('enter pk: '))
    n=Webpage.objects.get(pk=pk)
    date=input('enter date: ')
    a=input('enter author name: ')
    AO=Accessrecord.objects.get_or_create(name=n,date=date,autor=a)[0]
    AO.save()
    QLAO=Accessrecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

def display_capital(request):
    cn=input('enter capitalname: ')
    CO=capital.objects.get_or_create(cname=cn)[0]
    CO.save()
    QLCO=capital.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_capital.html',context=d)

def display_country(request):
    cun=input('enter country_name: ')
    pk=int(input('enter pk value of capita: '))
    cn=capital.objects.get(pk=pk)
    CUO=country.objects.get_or_create(country_name=cun,cname=cn)[0]
    CUO.save()
    QLCNO=country.objects.all()
    d={'QLCNO':QLCNO}
    return render(request,'display_country.html',d)

def newdisplaytopic(request):
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def newdisplaywebp(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    QLWO=Webpage.objects.all().order_by(Length('topic_name'))
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by('topic_name')
    QLWO=Webpage.objects.exclude(topic_name='cricket').order_by('topic_name')
    QLWO=Webpage.objects.exclude(topic_name='cricket').order_by('-url')
    QLWO=Webpage.objects.filter(Q(topic_name='rugby')& Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(Q(topic_name='rugby')| Q(url__endswith='in'))
    QLWO=Webpage.objects.filter(topic_name='rugby',url__endswith='in')
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') & Q(name__contains='n'))
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Q(topic_name='volleyball') & Q(name__endswith='i'))
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(name__contains='n'))

    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def newdisplayaccessr(request):
    QLAO=Accessrecord.objects.all()
    QLAO=Accessrecord.objects.all().order_by('name')
    QLAO=Accessrecord.objects.all().order_by('-name')
    QLAO=Accessrecord.objects.all().order_by(Length('name'))
    QLAO=Accessrecord.objects.filter(date='2023-12-02').order_by(Length('name'))
    QLAO=Accessrecord.objects.exclude(date='2023-12-02').order_by(Length('name'))
    QLAO=Accessrecord.objects.filter(autor__startswith='h')
    QLAO=Accessrecord.objects.filter(autor__endswith='a')
    QLAO=Accessrecord.objects.filter(pk__in=(2,4,5))
    QLAO=Accessrecord.objects.filter(pk__gt=2)
    QLAO=Accessrecord.objects.filter(pk__gte=2)
    QLAO=Accessrecord.objects.filter(pk__lt=5)
    QLAO=Accessrecord.objects.filter(pk__lte=5)
    QLAO=Accessrecord.objects.filter(autor__contains='n')
    QLAO=Accessrecord.objects.filter(date__lt='2023-12-02')
    QLAO=Accessrecord.objects.filter(date__year='2023')
    QLAO=Accessrecord.objects.filter(date__month='12')
    QLAO=Accessrecord.objects.filter(date__day='02')
    QLAO=Accessrecord.objects.filter(date__year__lt='2023')
    QLAO=Accessrecord.objects.filter(date__month__gte='01')
    QLAO=Accessrecord.objects.filter(date__day__lt='23')

    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

def update_webpage(request):
    Webpage.objects.filter(name='roopa').update(url='https://roopa.com')
    Webpage.objects.filter(topic_name='cricket').update(name='gill')
    ob=Topic.objects.get(topic_name='rugby')
    Webpage.objects.update_or_create(name='roopa',defaults={'email':'korean@gmail.com','topic_name':ob})
    obj=Topic.objects.get_or_create(topic_name='cricket')[0]
    Webpage.objects.update_or_create(name='haritha',defaults={'url':'https://haritha.com','topic_name':obj})
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)
