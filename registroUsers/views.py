from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User  # esta es la tabla de la base de datos proporcionada por django
from django.contrib.auth import login,logout,authenticate # metodos utilizados para el crud de los usuarios
from django.db import IntegrityError 
from django.contrib.auth.decorators import login_required



# esta es la pagina de inicio de la web 
# no es la definitiva

def home(request):
    return render(request,'home.html')


# registro y autenticacion de los usuarios 
def signup(request):
    
    #retorna el formularion de registro
    if request.method=='GET':    
        return render(request,'signup.html')
    else:
        #envia los datos del formulario por medio del metodo post
        
        if request.POST['password1']==request.POST['password2']:
            #  manejo de errores en la base de datos, se puede mejorar mucho más 
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
                user.save() # guarda el usuario en la base de datos
                login(request,user) # loguea automaticamente el usuario que ha sido creado
                return redirect('/')
            except IntegrityError: # manejo del error, este error pasa cuando un se intenta crear un usuario ya creado
                return render(request,'signup.html',{
                'error':'usuario ya existe'
                })
        # retorna nuevamente el formulario con un mensaje de erro si las contraseñas no coinciden
        return render(request,'signup.html',{
                'error':'contraseñas no coinciden'
                })


# funcion utilizada para desloguear un usuario
@login_required
def signout(request):
    logout(request)
    return redirect('/')



# fucion utilizada para iniciar sesion con un usuario ya creado

def signin(request):
    # retorna el formulario de logueo
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        # se utiliza para consultar en la base de datos si existe algun usuario creado con estos valores recibidos
        user=authenticate(
            request,username=request.POST['username'],password=request.POST['password']
            )
        # si no se encuentran el usuario retorna nuevamente el formulario con un error 
        if user is None:
             return render(request,'signin.html',{
             'error': 'usuario o contraseña incorrecto'
            })
        else:
            #si no se trae nuevamente esta funcion para loguear correctamente el usuario nuevamente
            login(request,user)
            return redirect('/',{'usuario':user.get_username})
            

   