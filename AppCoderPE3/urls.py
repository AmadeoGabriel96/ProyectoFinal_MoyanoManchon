from django.urls import path
from AppCoderPE3.views import *
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
    path("login/", iniciar_sesion, name="Iniciar Sesion"),
    path("about_me/", sobre_mi, name="Sobre Mi"),
    path("contact/", contacto, name="Contacto"),

    path("singup/", registrar, name="Registrar"),
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),
    path("edit/", editar_usuario, name="Editar Usuario"),
    path("contra/", CambiarContra.as_view(), name="Cambiar Contraseña"),
    path("avatar/", agregar_avatar, name="Cambiar Avatar"),

    path("", inicio, name="Inicio"),

    path("cursos/", curso), 
    path("profesores/", profesores), 
    path("alumnos/", alumnos), 

    path("crear_curso/", crear_curso, name="Cursos"),
    path("crear_profesor/", crear_profesor, name="Profesores"),
    path("crear_alumno/", crear_alumno, name="Alumnos"),

    path("buscar_curso/", buscar_curso),

    path("busqueda/", busqueda, name="Busqueda"),
    path("resultados/", resultados),

    path("leer_cursos/", leerCursos, name="cursos_leer"),
    path("leer_profes/", leerProfes, name="profes_leer"),
    path("leer_alumnos/", leerAlumnos, name="alumnos_leer"),

    path("eliminar_curso/<nombreCurso>", eliminarCurso, name="curso_eliminar"),
    path("eliminar_profe/<nombreProfe>", eliminarProfe, name="profe_eliminar"),
    path("eliminar_alumno/<nombreAlumno>", eliminarAlumno, name="alumno_eliminar"),

    path("editar_curso/<nombreCurso>", editarCurso, name="curso_editar"),
    path("editar_profesor/<nombreProfe>", editarProfesor, name="profe_editar"),
    path("editar_alumbi/<nombreAlumno>", editarAlumno, name="alumno_editar"),
]
