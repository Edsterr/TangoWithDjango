from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
     #return render(request, 'rango/index.html', context=context_dict)
     return HttpResponse(b"Rango says hey there partner!")

def about(request):
     #context_dict = {'boldmessage': "Help, information, and all that jazz"}
     #return render(request, 'rango/about.html', context=context_dict)
     return HttpResponse(b'Rango says here is the about page')
