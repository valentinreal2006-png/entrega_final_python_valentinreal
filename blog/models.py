from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre_prod = models.CharField(max_length=50)
    stock = models.IntegerField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre_prod


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} compró {self.producto}"
