from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Preparo,Tachada
from decimal import Decimal
from django.http import JsonResponse


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
        form = TachadaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            total_mariri = Decimal(request.POST.get('total_mariri'))
            total_chacrona = Decimal(request.POST.get('total_chacrona'))
            mariri_panela = Decimal(request.POST.get('mariri_panela'))
            chacrona_panela =Decimal(request.POST.get('chacrona_panela'))
            num_panelas = int(request.POST.get('qtde_panelas'))
            data = confereTachada(mariri_panela,chacrona_panela,num_panelas,total_mariri,total_chacrona)
            f.total_mariri = data[0]
            f.total_chacrona = data[1]
            f.save()
            messages.success(request, 'Dados gravados com sucesso')
        print(form.errors)
        
    
    obj = Preparo.objects.latest('id')
    print(obj)
    obj2 = validaTachada(obj)
    

    if obj2 is not None:
        form = TachadaForm(initial={'total_mariri':obj2.total_mariri,'total_chacrona':obj2.total_chacrona,'preparo':obj2.preparo,'num_tachada':obj2.num_tachada+1})
        context['form'] = form
        return render(request,template_name,context)

    else:
        form = TachadaForm(initial={'total_mariri':obj.total_mariri,'total_chacrona':obj.total_chacrona,'preparo':obj.dirigente,'num_tachada':1})
        context['form'] = form
        return render(request,template_name,context)


def edit_tachada(request, id_tachada):
    template_name = 'preparo/novaTachada.html'
    context = {}
    tachada = get_object_or_404(Tachada, id=id_tachada)
    if request.method == 'POST':
        form = TachadaForm(request.POST, instance=tachada)
        if form.is_valid():
            form.save()
            return redirect('cadastro:lista_tachada')
    form = TachadaForm(instance=tachada)
    context['form'] = form
    return render(request, template_name, context)

def delete_tachada(request, id_tachada):
    pass



class TachadaListView(ListView):
    model = Tachada
    context_object_name = 'tachadas'   # your own name for the list as a template variable
    queryset = Tachada.objects.all()
    template_name = 'preparo/listatachadas.html'  # Specify your own templ


def validaTachada(obj):
    obj2 = int(Tachada.objects.filter(preparo=obj.id).count())
    if obj2 != 0:
       obj2 = Tachada.objects.filter(preparo=obj.id).latest('id')
       return obj2
    return None


def confereTachada(mariri,chacrona,panelas,total_mariri,total_chacrona):
    if mariri is not None  and chacrona is not None:
        total_mariri -= (panelas * mariri)
        total_chacrona -= (panelas * chacrona)
        data = [total_mariri,total_chacrona]
        return data
    



    