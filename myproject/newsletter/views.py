from django.shortcuts import render, get_object_or_404, redirect 
from .models import Newsletter
from news.models import News 
from cat.models import Cat 
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
from trending.models import Trending 
#For login page 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User



#Create a Function for newslletter
#which saves the news using forms in master.html
def news_letter(request):

    if request.method == 'POST' :
        txt = request.POST.get('txt')

        b = Newsletter(txt=txt)
        b.save() 

        msg = "Your Email Received"
        return render(request , 'front/msgbox.html' , {'msg' : msg})
         

    return render(request , 'front/msgbox.html' , {'msg' : msg})
    


