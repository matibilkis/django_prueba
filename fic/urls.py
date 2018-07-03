from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/',views.AlumnoView.as_view(), name='alumnos'),
    path('alumnos/<int:pk>', views.AlumnoDetailView.as_view(), name='alumno-detail'),
    path('alumnos/create/', views.AlumnoCreate.as_view(), name='crea'),
    ]
