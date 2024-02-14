from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class DatosUsuarioInline(admin.StackedInline):
    model = models.DatosUsuario
    can_delete = False
    verbose_name = 'datos de usuario'


class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'rol')
    inlines = (DatosUsuarioInline,)
    fieldsets = (
        ('Credenciales de inicio de sesión', {
            'fields': (
                'username',
                'password',
                'rol'
            )
        }),
        ('Datos personales', {
            'fields': (
                'last_name',
                'first_name',
                'email'
            )
        }),
        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )

    add_fieldsets = (
        ('Credenciales de inicio de sesión', {
            'fields': (
                'username',
                'password1',
                'password2',
                'rol'
            )
        }),
        ('Datos personales', {
            'fields': (
                'last_name',
                'first_name',
                'email'
            )
        }),
        ('Permisos', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )


class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class SeccionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'carrera')
    list_filter = ('carrera',)


class ClaseAdmin(admin.ModelAdmin):
    list_display = ('materia', 'docente', 'seccion', 'dia',
                    'hora_inicio', 'hora_fin', 'aula')
    list_filter = ('materia', 'docente', 'seccion')


class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'clase')


admin.site.register(models.Usuario, UsuarioAdmin)
admin.site.register(models.Materia)
admin.site.register(models.Clase, ClaseAdmin)
admin.site.register(models.Inscripcion, InscripcionAdmin)
admin.site.register(models.Carrera, CarreraAdmin)
admin.site.register(models.Seccion, SeccionAdmin)
admin.site.register(models.Estado)
