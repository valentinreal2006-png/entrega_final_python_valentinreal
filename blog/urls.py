from django.urls import path
from blog.views import inicio, clientes, productos, compras, buscar_producto
from blog.views import home, page_list, page_detail

urlpatterns = [
    path("", inicio, name="inicio"),
    path('', home, name='home'),
    path("clientes/", clientes, name="clientes"),
    path("productos/", productos, name="productos"),
    path("compras/", compras, name="compras"),
    path("buscar/", buscar_producto, name="buscar_producto"),
    path('pages/', page_list, name='pages'),
    path('pages/<int:page_id>/', page_detail, name='page_detail'),
]
