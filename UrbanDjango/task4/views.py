from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def header_page(request):
    return render(request,'general_list.html')

def fist_page(request):
    return render(request,'fist_list.html')

def second_page(request):
    return render(request,'second_list.html')


