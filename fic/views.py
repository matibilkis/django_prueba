from django.shortcuts import render
from .models import Alumno
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    num_als=Alumno.objects.all().count()
    return render(
        request,
        'index.html',
         context={'num_als':num_als},
            )

class AlumnoView(generic.ListView):
    model = Alumno

class AlumnoDetailView(generic.DetailView):
    model = Alumno

class AlumnoCreate(CreateView):
    model = Alumno
    fields = '__all__'
    initial={}
