"""
URL configuration for AsISSSTE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', views.principal, name='principal'),
    path('registro/', views.registro_derechohabiente, name='registro'),
    path('actividades/', views.vista_actividades, name='vista_actividades'),
    path('asistencia/', views.lista_asistencia, name='lista_asistencia'),
    path('login/', views.inicia_sesion, name='login'),
    path('', views.inicio, name='inicio'),
    path('personas/', views.vista_personas, name='vista_personas'),
    path('asistencia/exportar_excel/', views.exportar_asistencia_excel, name='exportar_excel'),
    path("registro_actividad/", views.registrar_actividad, name="registro_actividad"),
    path('actividades/editar/<str:id_actividad>/', views.editar_actividad, name='editar_actividad'),
    path('actividades/eliminar/<str:id_actividad>/', views.eliminar_actividad, name='eliminar_actividad'),
    path('editar-persona/<str:id_personal>/', views.editar_persona, name='editar_persona'),
    path('eliminar-persona/<str:id_personal>/', views.eliminar_persona, name='eliminar_persona'),
    path('logout/', views.logout, name='logout'),

]
