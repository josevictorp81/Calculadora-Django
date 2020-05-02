from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def instrucoes(request):
    return render(request, 'instrucoes.html')

def subimit(request):
    entrada = request.GET['entrada']

    try:
        aux = eval(entrada)
        dicionario = {
            'entrada': entrada,
            'aux': aux,
            'error': False,
            'res': True
        }
        return render(request, 'index.html', context=dicionario)

    except:
        dicionario = {
            'error': True,
            'res': False
        }
        return render(request, 'index.html', context=dicionario)

    
