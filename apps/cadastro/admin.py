from django.contrib import admin
from .models import Preparo,Tachada,tipo_tachada
# Register your models here.

class PreparoAdmin(admin.ModelAdmin):
    list_display = ['data_inicio','dirigente', 'total_mariri', 'total_chacrona' ]
    search_fields = ['data_inicio','dirigente']
    list_filter = ['data_inicio']


admin.site.register(Preparo,PreparoAdmin)

class TachadaAdmin(admin.ModelAdmin):
    list_display = ['num_tachada','hora_entrada' ]
    search_fields = ['num_tachada','hora_entrada']
    list_filter = ['hora_entrada']


admin.site.register(Tachada,TachadaAdmin)

class TipoTachadaAdmin(admin.ModelAdmin):
    list_display = ['tipo' ]
    list_filter = ['tipo']

admin.site.register(tipo_tachada,TipoTachadaAdmin)