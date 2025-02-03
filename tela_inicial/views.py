from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def tela_inicial_view(request):
   return render(request, 'tela_inicial/index.html')
   
   
    
    
    
    
        

    