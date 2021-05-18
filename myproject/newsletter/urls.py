
from django.conf.urls import url 
from . import views 

urlpatterns = [

    url(r'^newsletter/submit/$' , views.news_letter , name = 'news_letter'),
   
    

    

]
