from django.shortcuts import render, redirect
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db_con
from datetime import datetime
from bson import ObjectId

# Create your views here.

def redireccion(request):
    return redirect('vista_prueba')

def vista_prueba(request):
    # Accede a una colección (ajusta el nombre según lo que creaste en Atlas)
    coleccion = db_con.db["personas"]  # o el  nombre real de la colección

    # Obtén todos los documentos, y convierte el cursor a lista
    documentos = list(coleccion.find())  # Opcional: elimina _id

    # Renderiza el template con los datos
    return render(request, 'prueba.html', {'datos': documentos})

def convertir_actividades(actividades):
    lista = []
    for act in actividades:
        lista.append({
            "nombre": act.get("nombre", ""),
            "horarios": act.get("horarios", [])
        })
    return lista

def registro_derechohabiente(request):
    actividades_col = db_con.db["actividades"]
    personas_col = db_con.db["personas"]

    if request.method == "POST":
        datos = {
            "nombre": request.POST.get("nombre"),
            "apellido": request.POST.get("apellido"),
            "edad": int(request.POST.get("edad")),
            "curp": request.POST.get("curp"),
            "telefono": request.POST.get("telefono"),
            "telefono_emergencia": request.POST.get("telefono_emergencia"),
            "correo": request.POST.get("correo"),
            "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
            "genero": request.POST.get("genero"),
            "actividad": request.POST.get("actividad"),
            "horario": request.POST.get("horario")
        }
        personas_col.insert_one(datos)
        return redirect("vista_prueba")

    actividades = list(actividades_col.find())
    actividades_json = convertir_actividades(actividades)
    return render(request, "registro.html", {"actividades": actividades_json})