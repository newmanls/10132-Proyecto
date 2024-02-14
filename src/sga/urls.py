from django.urls import path
from . import views

urlpatterns = [
    # urls generales
    path('', views.home, name='home'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),

    # urls para docentes
    path('u/2/clases/', views.DocenteClases.as_view(), name='docente_clases'),
    path('u/2/matricula/', views.DocenteMatricula.as_view(),
         name='docente_matricula'),
    path('u/2/matricula/<int:clase>',
         views.DocenteMatricula.as_view(), name='docente_matricula_clase'),

    # urls para alumnos
    path('u/3/clases/', views.AlumnoClases.as_view(), name='alumno_clases'),
    path('u/3/clases/inscribir/', views.AlumnoInscribirClase.as_view(),
         name='alumno_inscribir_clase'),
    path('u/3/clases/<int:pk>/retirar/', views.AlumnoRetirarClase.as_view(),
         name='alumno_retirar_clase'),
    path('u/3/solicitudes/', views.AlumnoSolicitudes.as_view(),
         name='alumno_solicitudes'),
]
