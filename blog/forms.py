from django import forms
from blog.models import Cliente, Producto, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_prod', 'stock', 'precio']


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'producto']


# FORMULARIO DE BÚSQUEDA
class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Buscar producto")
