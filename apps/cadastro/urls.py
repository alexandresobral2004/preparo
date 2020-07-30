"""preparo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from cadastro.views import PreparoListView,TachadaListView

app_name = 'cadastro'
urlpatterns = [
    path('preparo/adicionar', views.NovoPreparo,name='novo_preparo'),
    path('tachadas/add_tachada', views.NovaTachada,name='nova_tachada'),
    path('preparos/', PreparoListView.as_view(),name='lista_preparo'),
    path('tachadas/', TachadaListView.as_view(),name='lista_tachada'),
    path('edita/<int:id_tachada>/', views.edit_tachada,name='edita_tachada'),
    path('delete/<int:id_tachada>/', views.delete_tachada,name='delete_tachada'),
   
]