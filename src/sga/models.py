from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    roles = [
        (1, 'Administrador'),
        (2, 'Docente'),
        (3, 'Alumno'),
    ]

    username = models.IntegerField('cédula', unique=True)
    rol = models.IntegerField(
        'rol', choices=roles, default=roles[2][0])
    last_name = models.CharField('apellidos', max_length=150)
    first_name = models.CharField('nombres', max_length=150)

    REQUIRED_FIELDS = ['rol', 'last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def get_telefono(self):
        telefono = self.datosusuario.telefono
        return telefono if telefono else '---'

    def get_correo(self):
        correo = self.email
        return correo if correo else '---'


class Estado(models.Model):
    nombre = models.CharField('estado', max_length=100)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = 'estado'
        verbose_name_plural = 'estados'


class DatosUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefono = models.CharField('teléfono', max_length=50, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, blank=True)
    direccion = models.CharField('dirección', max_length=50, blank=True)

    def __str__(self):
        return f'{self.usuario}'

    class Meta:
        verbose_name = 'dato de usuario'
        verbose_name_plural = 'datos de usuarios'


class Carrera(models.Model):
    nombre = models.CharField('carrera', max_length=30, unique=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'


class Seccion(models.Model):
    codigo = models.CharField('código de sección', max_length=10)
    carrera = models.ForeignKey(
        Carrera, on_delete=models.CASCADE, verbose_name='carrera', default='')

    def __str__(self):
        return f'{self.carrera} {self.codigo}'

    class Meta:
        verbose_name = 'sección'
        verbose_name_plural = 'secciones'


class Materia(models.Model):
    nombre = models.CharField('materia', max_length=30, unique=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'


class Clase(models.Model):
    dias_de_la_semana = [
        ('lun', 'Lunes'),
        ('mar', 'Martes'),
        ('mie', 'Miércoles'),
        ('jue', 'Jueves'),
        ('vie', 'Viernes'),
        ('sab', 'Sábado')
    ]

    materia = models.ForeignKey(
        Materia, on_delete=models.CASCADE, verbose_name='materia')
    docente = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 2},
        verbose_name='docente')
    seccion = models.ForeignKey(
        Seccion, on_delete=models.CASCADE, verbose_name='sección')
    dia = models.CharField(
        'días', max_length=50, choices=dias_de_la_semana)
    hora_inicio = models.TimeField('hora de inicio')
    hora_fin = models.TimeField('hora de fin')
    aula = models.IntegerField('aula')

    def __str__(self):
        return f'{self.materia} ({self.seccion}) - {self.docente}'

    class Meta:
        verbose_name = 'clase'
        verbose_name_plural = 'clases'


class Inscripcion(models.Model):
    alumno = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 3},
        verbose_name='alumno')
    clase = models.ForeignKey(
        Clase, on_delete=models.CASCADE, verbose_name='clase')

    def __str__(self):
        return f'{self.alumno} - {self.clase}'

    class Meta:
        verbose_name = 'inscripción de materia'
        verbose_name_plural = 'inscripciones de materias'
