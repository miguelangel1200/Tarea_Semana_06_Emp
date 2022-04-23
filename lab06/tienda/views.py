from itertools import product
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Categoria, Producto

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_list = Categoria.objects.order_by('nombre')
    context = {'product_list':product_list, 'categoria_list':categoria_list}
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html', {'producto':producto})

def categoria(request, categoria_id):
    products = Producto.objects.filter(categoria=categoria_id)
    categoria_list = Categoria.objects.order_by('nombre')
    return render(request,'categoria.html', {'products':products,'categoria_list':categoria_list})