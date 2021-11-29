from enum import unique
from django.db import models

class Departamento(models.Model):
    id_dept = models.IntegerField(unique=True)
    ubicacion = models.CharField(max_length=30)
    estado_departamento = models.BooleanField()
    habitaciones = models.IntegerField()
    valor = models.IntegerField() 

    def __str__(self):
        return self.ubicacion 

class Cliente(models.Model):
    rut = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    correo = models.CharField(max_length=30)
    id_dept = models.ForeignKey(Departamento, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre 

class Administrador(models.Model):
    rut = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre 

class Servicios(models.Model):
    id_servicio = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=40)
    valor_servicio = models.FloatField()

    def __str__(self):
        return self.id_servicio


class Funcionario(models.Model):
    rut_funcionario = models.CharField(max_length= 20, unique=True)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre 


class Forma_pago(models.Model):
    tipo_pago = models.CharField(max_length=20)
    comprobante = models.CharField(max_length=40)

    def __str__(self):
        return self.tipo_pago

