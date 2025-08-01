from django.shortcuts import render, redirect
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db_con

# Create your views here.

from django.shortcuts import redirect

def redireccion(request):
    return redirect('vista_prueba')

def vista_prueba(request):
    # Accede a una colección (ajusta el nombre según lo que creaste en Atlas)
    coleccion = db_con.db["asissste"]  # o el nombre real de la colección

    # Obtén todos los documentos, y convierte el cursor a lista
    documentos = list(coleccion.find())  # Opcional: elimina _id

    # Renderiza el template con los datos
    return render(request, 'prueba.html', {'datos': documentos})