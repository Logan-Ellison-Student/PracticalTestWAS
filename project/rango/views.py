from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Page
def index(request):
    list=Page.objects.all()
    context_dict = {'news': list}

    return render(request, 'rango/index.html', context=context_dict)



