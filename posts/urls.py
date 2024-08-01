from django.contrib import admin
from django.urls import path
from posts import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('post/',views.postear, name='post'),
    path('reserve/',views.reservar, name='reserve'),
    path('perfil/',views.perfil, name= 'perfil'),
    path('perfil/<int:id>/', views.eliminar, name='eliminar'),
    path('perfil/editar/<int:id>/', views.editar, name='editar'),
    path('reserve/<int:id>/', views.reservas, name='reservar'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)