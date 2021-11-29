from django.shortcuts import render
from django.db import connection
import cx_Oracle
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login

def inicio(request):
    return render(request, "reservas/inicio.html")

def clientes(request):
    data = {
        'clientes': listado_clientes(),
        'departamento': listado_departamentos()
    }

    #guardar_datos('Mark', '20999888-1', '18/03/2002', 'mark@gmail.com', 982991100, 1)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rut = request.POST.get('rut')
        fecha_nac = request.POST.get('edad')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        id_dept = request.POST.get('departamento')
        salida = guardar_datos(nombre, rut, fecha_nac, correo, telefono, id_dept)
        if salida == 1:
            data['mensaje'] = 'Los datos se han registrado exitosamente'
            data['clientes'] = listado_clientes()
        else:
            data['mensaje'] = 'No se han podido ingresar los datos'

    return render(request, 'reservas/clientes.html', data)

def listado_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def listado_departamentos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_DEPARTAMENTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def guardar_datos(nombre, rut, fecha_nac, correo, telefono, id_dept):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_GUARDAR_DATOS', [nombre, rut, fecha_nac, correo, telefono, id_dept, salida])
    return salida.getvalue()

def login(request):
    return render(request, 'reservas/login.html')

def registrarse(request):
    return render(request, 'reservas/registrarse.html')

def iniciar_sesion(request):
    usuario = request.POST["usuario"]
    clave = request.POST["clave"]

    user = authenticate(request, username = usuario, password = clave)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('reserva:inicio'))
    else:
        return HttpResponse ("No se pudo autenticar las credenciales")