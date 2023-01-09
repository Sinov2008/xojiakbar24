import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
    if 'xo' in malumot.POST:
        matn = malumot.POST.get('xo')
        print(matn)
        soz = str(matn).strip()
        qidirish = Q(nomi__icontains = soz)|\
                   Q(malumot__icontains = soz)
        odamlar = Servise.objects.filter(qidirish)
        return render(malumot, 'index.html', {'ser': odamlar})

    elif 'xoji' in malumot.POST:
        matn = malumot.POST.get('xoji')
        print(matn)
        soz = str(matn).strip()
        qidirish = Q(ism__icontains = soz)|\
                   Q(lavozim__icontains = soz)|\
                   Q(malumot__icontains = soz)
        insonlar = Team.objects.filter(qidirish)
        return render(malumot, 'index.html', {'tem': insonlar})
    elif 'malumoti' in malumot.POST:
        matn = malumot.POST.get('malumoti')
        print(matn)
        soz = str(matn).strip()
        qidirish = Q(nomi__icontains = soz)|\
                   Q(cleant_nomi__icontains = soz)|\
                   Q(date__icontains = soz)|\
                   Q(link__icontains = soz)|\
                   Q(malumot__icontains = soz)|\
                   Q(tur__id__icontains = soz)
        ishlarimiz = Portfolio.objects.filter(qidirish)
        return render(malumot, 'index.html', {'works': ishlarimiz})
    elif 'llll' in malumot.POST:
        gmaill = malumot.POST.get('llll')
        Saqlash(gmail=gmaill).save()
    elif malumot.method =='POST':
        ismi = malumot.POST.get('name')
        gmaili = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        matn = malumot.POST.get('message')
        vaqti = datetime.datetime.now()
        Murojaat(name=ismi,gmail=gmaili,title=subject,text=matn,date=vaqti).save()

        ishlarimiz = Portfolio.objects.all()
        odamlar = Team.objects.all()
        insonlar = Servise.objects.all()
        return render(malumot,'index.html',{'works':ishlarimiz,'tem':odamlar,'ser':insonlar})
    if malumot.method == 'GET':
        odamlar = Team.objects.all()
        return render(malumot, 'index.html', {'tem': odamlar})

    elif malumot.method == 'GET':
        insonlar = Servise.objects.all()
        return render(malumot, 'index.html', {'ser':insonlar})

    else:
        ishlarimiz = Portfolio.objects.all()
        return render(malumot, 'index.html', {'works': ishlarimiz})

def kerak(malumot):
    return render(malumot,'inner-page.html')

def hoshim(malumot,id):
    if malumot.method =='POST':
        emaill = malumot.POST.get('el')
        Saqlash(gmail=emaill).save()

    shlarimiz = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':shlarimiz})
















