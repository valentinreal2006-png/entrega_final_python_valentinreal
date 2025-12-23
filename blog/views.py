from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, CompraForm, BuscarProductoForm
from blog.models import producto,cliente,Compra

def inicio(request):
    """Vista simple para la página de inicio."""
    return render(request, 'blog/inicio.html', {})


def clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clientes")
    else:
        form = ClienteForm()

    clientes = cliente.objects.all()

    return render(
        request,
        "blog/form_clientes.html",
        {
            "form": form,
            "clientes": clientes
        }
    )


def productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductoForm()
    else:
        form = ProductoForm()

    productos = producto.objects.all()

    return render(
        request,
        "blog/form_productos.html",
        {
            "form": form,
            "productos": productos,
        },
    )

def compras(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = CompraForm()

    return render(
        request,
        "blog/form_compras.html",
        {
            "form": form,
            "compras": Compra.objects.all()
        }
    )




# BUSQUEDA EN BD


def buscar_producto(request):
    productos = []  # ← SIEMPRE inicializada

    nombre = request.GET.get("nombre")

    if nombre:
        productos = producto.objects.filter(
            nombre_prod__icontains=nombre
        )

    return render(
        request,
        "blog/buscar_producto.html",
        {"productos": productos}
    )



def home(request):
    return render(request, "home.html")

def page_list(request):
    return render(request, "blog/page_list.html")

def page_detail(request, page_id):
    return render(request, "blog/page_detail.html", {"page_id": page_id})



