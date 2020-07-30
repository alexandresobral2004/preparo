from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Preparo(models.Model):
    data_inicio = models.DateField('Data do preparo',auto_now=False, auto_now_add=False)
    dirigente = models.CharField('M.Dirigente',max_length=100)
    assistente = models.CharField('M.Assistente',max_length=100)
    total_mariri = models.DecimalField('Total mariri',decimal_places=1,max_digits=5)
    total_chacrona = models.DecimalField('Total chacronai',decimal_places=1,max_digits=5)
    mariri_panela = models.DecimalField('Mariri/Panela',decimal_places=1,max_digits=5)
    chacrona_panela = models.DecimalField('Cacrona/Panela',decimal_places=1,max_digits=5)
    observacoes = models.TextField('Observações',max_length=250,blank=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Preparo'
        verbose_name_plural = 'Preparos'
        ordering = ['id']
     
    def __str__(self):
        return self.dirigente


class tipo_tachada(models.Model):
    tipo = models.CharField('Tipo Tachada',max_length=30)

    class Meta:
        verbose_name = 'tipo_tachada'
        ordering = ['id']
     
    def __str__(self):
        return self.tipo



class Tachada(models.Model):
    total_mariri = models.DecimalField('Total Mariri',decimal_places=1,max_digits=5,null=True)
    total_chacrona = models.DecimalField('Total Chacrona',decimal_places=1,max_digits=5,null=True)
    mariri_panela = models.DecimalField('Mariri/Panela',decimal_places=1,max_digits=5,null=True)
    chacrona_panela = models.DecimalField('Chacrona/Panela',decimal_places=1,max_digits=5,null=True)
    num_tachada = models.IntegerField('Num. Tachada',blank=False)
    qtde_panelas = models.IntegerField('Num. Panelas',blank=False)
    hora_entrada = models.TimeField('Hora Entrada',auto_now=False, auto_now_add=False,blank=False)
    hora_fervura = models.TimeField('Hora Fervura',auto_now=False, auto_now_add=False,null=True)
    hora_saida = models.TimeField('Hora Saída',auto_now=False, auto_now_add=False,null=True)
    agua_panela = models.DecimalField('Total água',decimal_places=1,max_digits=5,null=True)
    litros_vegetal = models.DecimalField('Litros Vegetal',decimal_places=1,max_digits=5,null=True)
    observacoes = models.TextField('Observações',max_length=250,null=True)
    tipo = models.ForeignKey(tipo_tachada,on_delete = models.CASCADE)
    preparo = models.ForeignKey(Preparo,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tachada'
        verbose_name_plural = 'Tachadas'
        ordering = ['id']
     
    def __str__(self):
        return self.hora_entrada

