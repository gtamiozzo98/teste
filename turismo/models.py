from django.db import models

def upload_image_restaurante(instance,filename):
    return f"{instance}-{filename}"

class Restaurante(models.Model):
    nome = models.CharField(max_length=300)
    cnpj = models.CharField(max_length=14,verbose_name='CNPJ')
    url = models.URLField(max_length = 300,verbose_name='Site')
    telefone = models.CharField(max_length=14,blank=True,null=True,verbose_name='Telefone')
    endereco = models.CharField(max_length=300,verbose_name='Endereço')
    img = models.ImageField(upload_to=upload_image_restaurante,blank=True,null=True)


    horarario_abre_segunda = models.TimeField(blank=True, null=True, verbose_name='Horário abre segunda')
    horarario_fecha_segunda = models.TimeField(blank=True, null=True, verbose_name='Horário abre segunda')

    horarario_abre_terca = models.TimeField(blank=True, null=True, verbose_name='Horário abre terça')
    horarario_fecha_terca = models.TimeField(blank=True, null=True, verbose_name='Horário fecha terça')

    horarario_fecha_quarta = models.TimeField(blank=True, null=True, verbose_name='Horário abre quarta')
    horarario_fecha_quarta= models.TimeField(blank=True, null=True, verbose_name='Horário fecha quarta')

    horarario_abre_quinta = models.TimeField(blank=True, null=True, verbose_name='Horário abre quinta')
    horarario_fecha_quinta = models.TimeField(blank=True, null=True, verbose_name='Horário fecha quinta')

    horarario_abre_sexta = models.TimeField(blank=True, null=True, verbose_name='Horário abre sexta')
    horarario_fecha_sexta = models.TimeField(blank=True, null=True, verbose_name='Horário fecha sexta')

    horarario_abre_sabado = models.TimeField(blank=True, null=True, verbose_name='Horário abre sábado')
    horarario_fecha_sabado = models.TimeField(blank=True, null=True, verbose_name='Horário fecha sábado')

    horarario_abre_domingo = models.TimeField(blank=True, null=True, verbose_name='Horário fecha domingo')
    horarario_fecha_domingo= models.TimeField(blank=True, null=True, verbose_name='Horário fecha domingo')

    #imagem = models.ImageField()
    def __str__(self):
        return self.nome

def upload_image_hotel(instance,filename):
    return f"{instance}-{filename}"
class Hotel(models.Model):
    nome = models.CharField(max_length=200,verbose_name='Nome')
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ')
    url = models.URLField(max_length=200, verbose_name='Site')
    telefone = models.CharField(max_length=14, blank=True, null=True, verbose_name='Telefone')
    endereco = models.CharField(max_length=300, verbose_name='Endereço')
    img = models.ImageField(upload_to=upload_image_hotel, blank=True, null=True)

    def __str__(self):
        return self.nome


def upload_image_atrativo(instance,filename):
    return f"{instance}-{filename}"
class Atrativo(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200,verbose_name='Endereço')
    descricao = models.TextField(max_length=1000,verbose_name='Descrição')
    img = models.ImageField(upload_to=upload_image_atrativo,blank=True,null=True)

    preco = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Valor', default=0, help_text='Ex: 25,00, o valor padrão é 0 ')
    horarario_abre_segunda = models.TimeField(blank=True, null=True, verbose_name='Horário abre segunda')
    horarario_fecha_segunda = models.TimeField(blank=True, null=True, verbose_name='Horário abre segunda')

    horarario_abre_terca = models.TimeField(blank=True, null=True, verbose_name='Horário abre terça')
    horarario_fecha_terca = models.TimeField(blank=True, null=True, verbose_name='Horário fecha terça')

    horarario_fecha_quarta = models.TimeField(blank=True, null=True, verbose_name='Horário abre quarta')
    horarario_fecha_quarta= models.TimeField(blank=True, null=True, verbose_name='Horário fecha quarta')

    horarario_abre_quinta = models.TimeField(blank=True, null=True, verbose_name='Horário abre quinta')
    horarario_fecha_quinta = models.TimeField(blank=True, null=True, verbose_name='Horário fecha quinta')

    horarario_abre_sexta = models.TimeField(blank=True, null=True, verbose_name='Horário abre sexta')
    horarario_fecha_sexta = models.TimeField(blank=True, null=True, verbose_name='Horário fecha sexta')

    horarario_abre_sabado = models.TimeField(blank=True, null=True, verbose_name='Horário abre sábado')
    horarario_fecha_sabado = models.TimeField(blank=True, null=True, verbose_name='Horário fecha sábado')

    horarario_abre_domingo = models.TimeField(blank=True, null=True, verbose_name='Horário fecha domingo')
    horarario_fecha_domingo= models.TimeField(blank=True, null=True, verbose_name='Horário fecha domingo')


    def __str__(self):
        return self.nome

def upload_image_evento(instance,filename):
    return f"{instance}-{filename}"

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=200)
    dia_inicio = models.DateField(verbose_name='Dia Início')
    dia_final = models.DateField(null=True,blank=True)
    horario_inicial = models.TimeField()
    horario_termina = models.TimeField(null=True,blank=True)
    url = models.URLField(max_length=300, verbose_name='Site do Evento')
    preco = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Valor',help_text='Ex: 25.00',null=True,blank=True)
    descricao = models.TextField(max_length=1000,verbose_name='descrição')
    img = models.ImageField(upload_to=upload_image_evento,blank=True,null=True)


    def __str__(self):
        return self.nome
