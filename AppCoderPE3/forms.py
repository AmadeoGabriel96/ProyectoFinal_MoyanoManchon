from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.camada}"

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesión = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()

class AlumnoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()  

class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()  

class RegistroUsuario(UserCreationForm):

    class Meta:

        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"] 

class EdicionUsuario(UserChangeForm):

    password = None

    class Meta:

        model = User
        fields = [ "email", "first_name", "last_name",]        

     
