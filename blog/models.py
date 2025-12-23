from django.db import models
from django.contrib.auth.models import User

from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class producto(models.Model):
    nombre_prod = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    def __str__(self):
        return self.nombre_prod


class Compra(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Page(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to="pages/")
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"