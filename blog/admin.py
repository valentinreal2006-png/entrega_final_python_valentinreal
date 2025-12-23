# Register your models here.
from django.contrib import admin
from .models import cliente, producto, Compra, Avatar

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(Compra)
admin.site.register(Avatar)