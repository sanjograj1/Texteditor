from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc= request.POST.get('removepunc', 'off')
    caps=request.POST.get('caps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    if removepunc =='on':
        h=""
        for i in djtext:
            if i not in ''';,:,.,!,?",',-,[],(),/,''':
                h=h+i
        djtext=h

    if caps =='on':
        h=""
        for j in djtext:
            h=h+j.upper()
        djtext = h
    if newlineremover =='on':
        h=""
        for j in djtext:
            if j!='\n' and j!='\r':
                h=h+j
        djtext = h
    if removepunc!='on' and caps!='on' and newlineremover!='on':
        return HttpResponse("Please select one option")

    para={'purpose':'sentence','analyse_text':djtext}
    return render(request,'analyse.html',para)

def about(request):
    return render(request, 'about.html')
def contactus(request):
    return render(request, 'contactus.html')