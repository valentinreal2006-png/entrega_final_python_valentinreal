"""
URL configuration for BlogProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# túproyecto/urls.py (Archivo principal de URLs)

from django.contrib import admin
from django.urls import path, include
# Asegúrate de importar las vistas de tu app 'blog'
from blog import views 

urlpatterns = [
    # 1. RUTA DE ADMINISTRACIÓN
    path('admin/', admin.site.urls),
    
    # 2. RUTA DE INICIO (HOME o Raíz)
    # Patrón: '' (URL vacía). Nombre: 'inicio'
    # Esta línea soluciona el error en la captura_51953d.png (URL solicitada: http://127.0.0.1:8000/)
    path('', views.inicio, name='inicio'), 
    
    # 3. RUTA EXPLÍCITA PARA /inicio/
    # Patrón: 'inicio/'. Nombre: 'inicio_explícito' (para evitar conflictos)
    # Esta línea soluciona el error en la captura_837b78.png (URL solicitada: http://127.0.0.1:8000/inicio/)
    path('inicio/', views.inicio, name='inicio_explícito'),

    # 4. RUTAS RESTANTES (Asumiendo que las vistas existen en blog/views.py)
    path('clientes/', views.clientes, name='clientes'), 
    path('productos/', views.productos, name='productos'),
    path('compras/', views.compras, name='compras'),
    path('buscar/', views.buscar_producto, name='buscar'), 
]
