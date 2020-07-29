from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Preparo,Tachada


from .forms import PreparoForm,TachadaForm




class PreparoListView(ListView):
    model = Preparo
    template_name = 'preparo/listapreparos.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.all()
        #(\usuario=self.request.user)


def NovoPreparo(request):
    template_name = 'preparo/novo_preparo.html'
    context = {}
    if request.method == 'POST':
        form = PreparoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.usuario = request.user
            f.save()
            messages.success(request, 'Dados gravados com sucesso')
    form = PreparoForm()
    context['form'] = form
    return render(request, template_name, context)


def NovaTachada(request):
    template_name = 'preparo/novaTachada.html'
    context = {}
    if request.method == 'POST':
        form = PreparoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.preparo = form.
            f.save()
            messages.success(request, 'Dados gravados com sucesso')
    form = PreparoForm()
    context['form'] = form
    return render(request, template_name, context)






    