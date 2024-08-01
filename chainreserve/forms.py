from django.forms import ModelForm
from posts.models import posts
from django import forms


class postForm(forms.ModelForm):
    class Meta:
        model= posts
        fields = [
            'propiedad',
            'titulo',
            'ubicacion',
            'descripcion',
            'precio'
        ]
class postForm2(forms.ModelForm):
    class Meta:
        model= posts
        fields = [
            'titulo',
            'ubicacion',
            'descripcion',
            'precio'
        ]
        