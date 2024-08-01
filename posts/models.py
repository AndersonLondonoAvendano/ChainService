from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class posts(models.Model):
    propiedad=models.ImageField(upload_to='images/', null=True)
    titulo=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)
    descripcion=models.TextField()
    precio=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titulo} - {self.ubicacion}"
    
    def delete(self, using=None,keep_parents=False):
        self.propiedad.storage.delete(self.propiedad.name)
        super().delete()
        