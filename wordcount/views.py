from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator


def home(request):
    return render(request,'home.html')


def count(request):

    ftxt= request.GET['txt']
    wrdlist=ftxt.split()


    trans = Translator()
    t = trans.translate(
    ftxt, src= 'en', dest='ta'
    )
    ans = t.text
    #print(f'Source: {t.src}')
    #print(f'Destination: {t.dest}')
    #print(f'{t.origin} -> {t.text}')
    #print()



    return render(request,'count.html',{'word':ans} )
