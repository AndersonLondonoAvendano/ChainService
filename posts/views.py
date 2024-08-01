from django.shortcuts import render,redirect,get_object_or_404
from chainreserve.forms import postForm,postForm2
from .models import posts
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




# vista utilizada para publicacion de inmuebles
@login_required
def postear(request):
    # obtiene el formulario 
    formulario= postForm(request.POST or None,request.FILES or None)
    
    # si los datos enviados al formulario son correctos se envian  hacia la BD
    # si no se renderiza nuevamente el formulario
    
    if formulario.is_valid():
        new=formulario.save(commit=False)
        new.user = request.user
        new.save()
        return redirect('perfil')
    else:
        return render(request,'posts.html',{
        'formulario': formulario,
    })


# vista de reserva de inmuebles
def reservar(request):
    post=posts.objects.all() # se obtiene todos los objetos de la base de datos en donde se encuentran las publicaciones
    return render(request,'reservas.html',{
        'post': post # se guardan todos los datos en esta variable para luego iterarlos con un bucle for
    })               # y asi poder mostrar todas las publicaciones realizadas por todos los usuarios



# vista del perfil 
@login_required
def perfil(request):
    user=request.user # se utiliza para obtener el usuario
    post=posts.objects.filter(user=request.user) # con esto se esta realizando un consulta la cual muestra unicamente las 
    return render(request,'perfil.html',{        # publicaciones  pertenecientes a el usuario obtenido
        'user': user,
        'post':post  # nuevamente se guardan todos los datos en esta variable para luego iterarlos con un bucle for
    })               # y asi poder mostrar unicamente las publicaciones relacionadas con el usuario


# eliminar una publicacion 
@login_required
def eliminar(request,id):
    publicacion=get_object_or_404(posts,pk=id,user=request.user)  # se utiliza  para poder obtener el id de la publicacion y poder mostrarla en la url
                                                                  # lo que nos permite poder eliminar solo esa publicacion
    publicacion.delete()# se elimina lo obtenido anteriormente                
    return redirect('perfil')

# editar una publicacion
@login_required
def editar(request,id):
    # si el request es get se realiza lo siquiente
    if request.method == 'GET': 
        publicacion=get_object_or_404(posts,pk=id)  # se obtiene el objeto del modelo post con su pk 
        form= postForm2(instance=publicacion) # se trae el formulario del modelo de la bd y se instancia con lo obtenido anteriormente
        return render(request, 'editar.html',{'form':form,'publicacion':publicacion}) # se retorna en el front el formulario con los datos
    else:
        # si el request es post se realiza lo siguiente
        publicacion=get_object_or_404(posts,pk=id) # se obtienen los datos actualizados del objeto del modelo
        update=postForm(request.POST,instance=publicacion) # se actualiza por el metodo POST
        update.save() # se guardan los cambios
        return redirect('perfil') # si el proceso fue correcto redirecciona a la pagina del perfil


# reservar un inmueble
@login_required
def reservas(request,id):
    publicacion=get_object_or_404(posts,pk=id) # se obtiene nuevamente el objeto del modelo post con su pk
    return render(request, 'reservar.html',{'publicacion':publicacion}) # se pasan al front esos datos para luego utilizarlos en un card

