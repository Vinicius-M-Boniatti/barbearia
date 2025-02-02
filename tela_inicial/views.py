from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def tela_inicial_view(request):
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        return render(request, 'tela_inicial/index.html')

    
    
        

    