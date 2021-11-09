from django import forms

from .models import Boletim

class PostForm(forms.ModelForm):


    class Meta:
        model = Boletim
        fields = ('nota1', 'nota2', 'nota3', 'nota4')
