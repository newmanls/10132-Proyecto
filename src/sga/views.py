from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import View, ListView, CreateView, DeleteView, TemplateView
from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from . import models


class RoleTestMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.rol == self.required_role

    def handle_no_permission(self):
        raise Http404('Página no encontrada')


@login_required
def home(request):
    match request.user.rol:
        case 1:
            return redirect('admin/')
        case 2:
            return redirect('docente_clases')
        case 3:
            return redirect('alumno_clases')
        case _:
            return redirect('login')


class DocenteClases(RoleTestMixin, ListView):
    required_role = 2
    model = models.Clase
    template_name = 'user/teacher/classes.html'

    def get_queryset(self):
        return models.Clase.objects.filter(docente=self.request.user)


class DocenteMatricula(RoleTestMixin, View):
    required_role = 2
    template_name = 'user/teacher/enrollments.html'

    def get(self, request, clase=None):
        clases = models.Clase.objects.filter(docente=request.user)
        context = {'clases': clases}

        if clase is not None:
            if not clases.filter(id=clase):
                raise Http404('Clase no encontrada')
            else:
                alumnos = models.Inscripcion.objects.filter(clase__id=clase)
                context['inscripcion_list'] = alumnos
                context['clase_id'] = clase
                clase_model = models.Clase.objects.get(id=clase)
                clase_display = f'{clase_model.materia} ({clase_model.seccion})'
        else:
            clase_display = 'Seleccionar materia'
        context['clase_display'] = clase_display

        return render(request, self.template_name, context)


class AlumnoClases(RoleTestMixin, ListView):
    required_role = 3
    model = models.Inscripcion
    template_name = 'user/student/classes.html'

    def get_queryset(self):
        return models.Inscripcion.objects.filter(alumno=self.request.user)


class AlumnoInscribirClase(RoleTestMixin, CreateView):
    required_role = 3
    model = models.Inscripcion
    template_name = 'form_simple.html'
    fields = ['clase']
    success_url = reverse_lazy('alumno_clases')

    def form_valid(self, form):
        form.instance.alumno = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['clase'].queryset = models.Clase.objects.exclude(
            inscripcion__alumno=self.request.user)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Inscribir clase'
        return context


class AlumnoRetirarClase(RoleTestMixin, DeleteView):
    required_role = 3
    model = models.Inscripcion
    success_url = reverse_lazy('alumno_clases')


class AlumnoSolicitudes(RoleTestMixin, TemplateView):
    required_role = 3
    template_name = 'user/student/requests.html'


class Perfil(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
