from django import forms
from blog.models import cliente, producto, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'telefono', 'email']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre_prod', 'stock', 'precio']


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'producto', 'cantidad']


# FORMULARIO DE BÚSQUEDA
class BuscarProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Buscar producto")
