from django.contrib import admin
from .models import Cliente, Administrador, Departamento, Forma_pago, Servicios, Funcionario

admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Departamento)
admin.site.register(Funcionario)
admin.site.register(Servicios)
admin.site.register(Forma_pago)
