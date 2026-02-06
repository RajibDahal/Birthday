from django.shortcuts import render
from django.http import HttpResponse
def home(request):
   return HttpResponse('<h1>Hey i am Rajib Dahal.</h1>')

#def sucess_page(request):
 #   return HttpResponse('<h1>Hey this is success page.</h1>')

def happy_birthday(request):
    return render(request, 'birthday.html')

def home(request):
    return render(request, "home.html")
