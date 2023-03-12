from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def display(request):
  messages.info(request,'info application')
  return render(request,'info.html')
