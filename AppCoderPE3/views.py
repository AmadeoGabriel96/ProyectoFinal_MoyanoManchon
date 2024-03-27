from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from AppCoderPE3.forms import *
from AppCoderPE3.models import * 

# Create your views here.

def inicio(request):

    return render(request,"AppCoderPE3/inicio.html", {"mensaje":"Bienvenido a la academia"})

def sobre_mi(request):

    return render(request, "AppCoderPE3/sobre_mi.html") 

def contacto(request):

    return render(request, "AppCoderPE3/contacto.html") 

def iniciar_sesion(request):
    
    if request.method == "POST":
            
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            usuario = authenticate(username=info_dic["username"], password=info_dic["password"])

            if usuario is not None: 
                        
                login(request, usuario)
                        
                return redirect("Inicio")

        else: 
                
            return render(request, "AppCoderPE3/inicio.html", {"mensaje":"Usuario o contraseña incorrectos"})
        
    else:

        formulario = AuthenticationForm()

    return render(request, "AppCoderPE3/iniciar_sesion.html", {"form":formulario,"mensaje":""})  

def registrar(request):

    formulario = RegistroUsuario() 

    if request.method == "POST": 

        formulario = RegistroUsuario(request.POST)

        if formulario.is_valid():

            formulario.save()

            return render(request, "AppCoderPE3/inicio.html", {"mensaje":"El usuario fue creado con éxito"}) 

    return render(request, "AppCoderPE3/registro.html", {"form":formulario})

def cerrar_sesion(request):

    logout(request)

    return render(request, "AppCoderPE3/inicio.html") 

@login_required
def editar_usuario(request):

    usuario = request.user

    formulario = EdicionUsuario(initial={"email":usuario.email,
                                         "first_name":usuario.first_name,
                                         "last_name":usuario.last_name,})

    if request.method == "POST":
        
        formulario = EdicionUsuario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            usuario.email=info_dic["email"],
            usuario.first_name=info_dic["first_name"],
            usuario.last_name=info_dic["last_name"],

            usuario.save()

            return render(request, "AppCoderPE3/inicio.html")

        else: 

            formulario = EdicionUsuario(initial={"email":usuario.email,
                                                 "first_name":usuario.first_name,
                                                 "last_name":usuario.last_name,})    

    return render(request, "AppCoderPE3/editar_usuario.html", {"form":formulario}) 

@login_required
def agregar_avatar(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():

            usuario_actual = request.user
            nuevo_avatar = Avatar(usuario=usuario_actual, imagen=formulario.cleaned_data["imagen"])

            nuevo_avatar.save()

            return render(request, "AppCoderPE3/inicio.html")
    else:
        
        formulario = AvatarFormulario()
    
    return render(request, "AppCoderPE3/nuevo_avatar.html", {"form": formulario})

def curso(request):

    return render(request,"AppCoderPE3/cursos.html")  

def profesores(request):

    return render(request,"AppCoderPE3/profesores.html")

def alumnos(request):

    return render(request,"AppCoderPE3/alumnos.html") 

@login_required
def crear_curso(request):

    if request.method =="POST":

        curso_nuevo = Curso(
            nombre=request.POST["nombre"],
            camada=request.POST["camada"])

        curso_nuevo.save()

        return render(request,"AppCoderPE3/inicio.html")

    return render(request, "AppCoderPE3/crear_curso.html")  

@login_required
def crear_profesor(request):

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            profesor_nuevo = Profesor(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                edad=info_dic["edad"],
                email=info_dic["email"],
                profesión=info_dic["profesión"],
            )

            profesor_nuevo.save()

            return render(request, "AppCoderPE3/crear_profesor.html")

    else: 

        formulario = ProfesorFormulario()

    return render(request, "AppCoderPE3/crear_profesor.html", {"form":formulario})    

@login_required
def crear_alumno(request):

    if request.method == "POST":

        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            alumno_nuevo = Alumno(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                edad=info_dic["edad"],
                email=info_dic["email"],
            )

            alumno_nuevo.save()

            return render(request, "AppCoderPE3/crear_alumno.html")

    else: 

        formulario = AlumnoFormulario()

    return render(request, "AppCoderPE3/crear_alumno.html", {"form":formulario})

def buscar_curso(request):

    if request.GET:

        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)

        mensaje = f"Estás buscando el curso: {nombre}"
   
        return render(request, "AppCoderPE3/buscar_curso.html", {"resultados":cursos})

    
    return render(request, "AppCoderPE3/buscar_curso.html")

def busqueda(request):

    return render(request, "AppCoderPE3/busqueda.html")    

def resultados(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoderPE3/resultados.html", {"cursos":cursos, "camada":camada})

    else: 

        respuesta = "No enviaste datos."    

    return HttpResponse(respuesta)

def leerCursos(request):

    cursos = Curso.objects.all()

    contexto = {"cursos": cursos}

    return render(request, "AppCoderPE3/leer_cursos.html", contexto)

def leerProfes(request):

    profesores = Profesor.objects.all()

    contexto = {"profes": profesores}

    return render(request, "AppCoderPE3/leer_profes.html", contexto)

def leerAlumnos(request):

    alumnos = Alumno.objects.all()

    contexto = {"alumnos": alumnos}

    return render(request, "AppCoderPE3/leer_alumnos.html", contexto)  

def eliminarCurso(request, nombreCurso):

    curso = Curso.objects.get(nombre=nombreCurso)

    curso.delete()

    cursos = Curso.objects.all()

    contexto = {"cursos": cursos}   

    return render(request, "AppCoderPE3/leer_cursos.html", contexto) 

def eliminarProfe(request, nombreProfe):

    profesor = Profesor.objects.get(nombre=nombreProfe) 
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"profes": profesores}   

    return render(request, "AppCoderPE3/leer_profes.html", contexto)

def eliminarAlumno(request, nombreAlumno):

    alumno = Alumno.objects.get(nombre=nombreAlumno) 
    alumno.delete()

    alumnos = Alumno.objects.all()

    contexto = {"alumnos": alumnos}   

    return render(request, "AppCoderPE3/leer_alumnos.html", contexto)  

def editarCurso(request, nombreCurso):

    curso = Curso.objects.get(nombre=nombreCurso)

    formulario = CursoFormulario(initial={"nombre":curso.nombre, "camada":curso.camada}) 

    if request.method == "POST": 

        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            curso.nombre = info_dic["nombre"]
            curso.camada = info_dic["camada"]

            curso.save()

            return render(request, "AppCoderPE3/inicio.html")

        else:

            formulario = CursoFormulario(initial={"nombre":curso.nombre, "camada":curso.camada}) 

    return render(request, "AppCoderPE3/editar_curso.html", {"form":formulario, "nombre": nombreCurso})     

def editarProfesor(request, nombreProfe):

    profesor = Profesor.objects.get(nombre=nombreProfe)

    formulario = ProfesorFormulario(initial={"nombre":profesor.nombre, 
                                             "apellido":profesor.apellido,
                                             "edad":profesor.edad, 
                                             "profesión":profesor.profesión, 
                                             "email":profesor.email})

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            profesor.nombre = info_dic["nombre"]
            profesor.apellido = info_dic["apellido"]
            profesor.edad = info_dic["edad"]
            profesor.profesión = info_dic["profesión"]
            profesor.email = info_dic["email"]

            profesor.save()

            return render(request, "AppCoderPE3/inicio.html")
        
        else: 

            formulario = ProfesorFormulario(initial={"nombre":profesor.nombre, 
                                                     "apellido":profesor.apellido,
                                                     "edad":profesor.edad, 
                                                     "profesión":profesor.profesión, 
                                                     "email":profesor.email})

    return render(request, "AppCoderPE3/editar_profesor.html", {"form":formulario, "nombre":nombreProfe}) 

def editarAlumno(request, nombreAlumno):

    alumno = Alumno.objects.get(nombre=nombreAlumno)

    formulario = AlumnoFormulario(initial={"nombre":alumno.nombre, "apellido":alumno.apellido,
            "edad":alumno.edad, "email":alumno.email})

    if request.method == "POST":

        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            alumno.nombre = info_dic["nombre"]
            alumno.apellido = info_dic["apellido"]
            alumno.edad = info_dic["edad"]
            alumno.email = info_dic["email"]

            alumno.save()

            return render(request, "AppCoderPE3/inicio.html")
        
        else: 

            formulario = AlumnoFormulario(initial={"nombre":alumno.nombre, 
                                                   "apellido":alumno.apellido,
                                                   "edad":alumno.edad, 
                                                   "email":alumno.email})

    return render(request, "AppCoderPE3/editar_alumno.html", {"form":formulario, "nombre":nombreAlumno}) 

class CambiarContra(LoginRequiredMixin, PasswordChangeView):

    template_name = "AppCoderPE3/cambiar_contraseña.html"
    success_url = "/AppCoderPE3/"



           




    
  









 
