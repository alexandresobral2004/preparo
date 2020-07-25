from django.shortcuts import render,redirect
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    template_name = 'index.html'
    return render(request, template_name,{})