from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def display(request):
  return render(request,'calc.html',{'name':'shubham'})

def add (request):
  n1 = int(request.POST['num1'])
  n2 = int(request.POST['num2'])
  opr = str(request.POST['oper'])

  if request.method == 'POST':
    if opr == '+':
      res = n1+n2

    elif opr == '-':
      res = n1-n2

    elif opr == '*':
      res = n1*n2

    elif opr == '/':
      res = n1/n2

    else:
      messages.error(request,'Invalid Operator')
      return render(request,'res.html',{'result':'Enter a valid operator'})
    
    return render(request,'res.html',{'result':res})


