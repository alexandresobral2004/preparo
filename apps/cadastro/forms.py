from django import forms
from django.contrib.auth.models import User
from .models import Preparo,Tachada,tipo_tachada


class preparoForm(forms.ModelForm):
    
    class Meta:
        model = Preparo
        exclude = ('usuario',)


class TachadaForm(forms.ModelForm):

    class Meta:
        model = Tachada
        