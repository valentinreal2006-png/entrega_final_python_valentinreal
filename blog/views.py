from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, CompraForm, BuscarProductoForm
from .models import Producto

def inicio(request):
    """Vista simple para la página de inicio."""
    return render(request, 'blog/inicio.html', {})

def clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ClienteForm()
    return render(request, "blog/form_clientes.html", {"form": form})

def productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = ProductoForm()
    return render(request, "blog/form_productos.html", {"form": form})

def compras(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = CompraForm()
    return render(request, "blog/form_compras.html", {"form": form})


# BUSQUEDA EN BD
def buscar_producto(request):
    productos = []
    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        productos = Producto.objects.filter(nombre_prod__icontains=nombre)

    form = BuscarProductoForm()
    return render(request, "blog/buscar_producto.html", {"form": form, "productos": productos})
