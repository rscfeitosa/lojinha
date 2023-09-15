from django.shortcuts import render, redirect
from sistema.formulario import ProdutoForm
from sistema.models import Produto

def home(request):
   data = {}
   data['db'] = Produto.objects.all()
   return render (request, "index.html", data)

def cadastro(request):
   data={}
   data['formulario'] = ProdutoForm()
   return render (request, "produto.html", data)

def conexao(request):
   cadastro = ProdutoForm(request.POST or None)
   if cadastro.is_valid():
      cadastro.save()
      return redirect ('home')
   else:
      return redirect ('home')
      

def view(request, pk):
   data={}
   data['db'] = Produto.objects.get(pk=pk)
   return render (request, 'view.html', data)