from django import forms
from django.contrib.auth.models import User
from .models import Preparo,Tachada,tipo_tachada
from bootstrap_datepicker_plus import DatePickerInput


class PreparoForm(forms.ModelForm):
    data_inicio = forms.DateField(widget=DatePickerInput(format='%d/%m/%Y'))
    class Meta:
        model = Preparo
        exclude = ('usuario',)


class TachadaForm(forms.ModelForm):

    class Meta:
        model = Tachada
        fields = '__all__'
        