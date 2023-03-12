from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

"""def january(request):
  return HttpResponse('First month of the year')

def february(request):
  return HttpResponse('shortest month of the year')

def march(request):
  return HttpResponse(' month of Exams')"""

#OR

"""def months(request, month): # additional arg= takes that arg to the urls path
    
  if month == 'january':
    msg = "First month of the year"

  elif month == 'february':
    msg = "shortest month of the year"

  elif month == 'january':
    msg = "Exam month of the year"

  else:
    return(HttpResponseNotFound('invalid month'))
  
  return HttpResponse(msg)"""

d={
  'january':'First month of the year',
  'february':'Shorthest month of the year',
  'march':' month of the exam',
  'april':None,
  'may':'month of vaccation',
  'june':'month of admission',
  'july':'longest month',
  'august':'NO non-veg month',
  'september':'ganpati baapa morya',
  'october':'month of dushara',
  'november':'month of lights',
  'december':None,
}

def index(request):
  l = list(d)
  return render(request,'index.html', {'data':l})



def month_with_num(request,month):
  l= list(d)
  data = l[month-1]
  red_path = reverse('disp',args=[data])
  #return HttpResponseRedirect('/month/'+data) 
  return HttpResponseRedirect(red_path) 


def months(request, month):
  try:
    #return HttpResponse(d[month])
    return render(request,'month.html',{'message':d[month],'m':month})
  except:
    return HttpResponseNotFound("Invalid month name")