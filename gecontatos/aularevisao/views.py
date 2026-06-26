from django.shortcuts import render
from aularevisao.models import Pessoa

# Create your views here.

def index(request):
    context = {}
    context['nome'] = 'Primeira variável'

    todaspessoas= Pessoa.objects.all()
    context['todaspessoas'] = todaspessoas
    return render(request,"paginaprincipal.html",context)
