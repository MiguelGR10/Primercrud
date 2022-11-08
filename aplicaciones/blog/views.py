from django.shortcuts import render
from .models import Post, categoria, Autor
from django.http import HttpResponse
from django.core import serializers

def lista(request):
    listas = serializers.serialize('json', categoria.objects.all())
    #return HttpResponse(serialize('json', use_natural_foreign_keys = True), 'application/json')

    return HttpResponse(listas, content_type='application/json')

def home(request):

    potss=Post.objects.filter(estado= True)
    return render(request, 'index.html', {"publi":potss})

def post(request, slug):
    potst=Post.objects.get(
        slug = slug
    )
    print(potst)
    return render(request, 'post.html', {'detalle_post':potst})

def categorias(request):
    cate=categoria.objects.filter(estado= True)
    print(cate)
    
    return render(request, 'categorias.html', {"catego":cate})

def posst(request):
    prueba=Post.objects.filter(estado= True)
    return render(request, 'case.html', {"publi":prueba})



