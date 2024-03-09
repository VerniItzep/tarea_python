from django.shortcuts import render, redirect
from .models import Task

def lista_alumnos(request):
    tasks = Task.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': tasks})

def crear_alumno(request):
    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombres', '')  # Obtener el nombre del campo del formulario
        nuevo_apellido = request.POST.get('apellidos', '')  # Obtener el apellido del campo del formulario
        nuevo_email = request.POST.get('email', '')  # Obtener el email del campo del formulario
        
        if nuevo_nombre and nuevo_apellido and nuevo_email:
            nuevo_alumno = Task(nombre=nuevo_nombre, apellido=nuevo_apellido, email=nuevo_email)
            nuevo_alumno.save()
            return redirect('lista_alumnos')
        else:
            error = 'Todos los campos son obligatorios.'
            return render(request, 'alumnos/crear_alumno.html', {'error': error})
    else:
        return render(request, 'alumnos/crear_alumno.html')

def eliminar_alumno(request, task_id):
    alumno = Task.objects.get(id=task_id)  
    alumno.delete()
    return redirect('lista_alumnos')
