from django.urls import path
from . import views

"""urlpatterns = [
  path('january', views.january),  
  path('february', views.february),
  path('march', views.march),   #the url in the string will be our url name in the main url of page with / fn in the end
]"""

#OR

urlpatterns = [
  path('',views.index, name='index'),
  path('/<int:month>', views.month_with_num), #if integer is entered it will go for fn month_with_n
  path('/<str:month>', views.months, name='disp'), #<month> here is forwarded to views month  str= if the i/p is string it will go to views
]