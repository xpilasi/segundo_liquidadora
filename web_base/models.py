from distutils.errors import LibError
from tabnanny import verbose
from time import timezone
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from datetime import datetime,date, time
from django.utils import timezone



# Create your models here.

class TipoVehiculo(models.Model):
    
    cod_vehiculo = models.CharField(max_length=100, null=False,verbose_name="Código vehículo")
    tipo_vehiculo = models.CharField(max_length=100, null=False,verbose_name="Tipo vehículo")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Tipo de vehículo'
        verbose_name_plural = 'Tipos de vehículos'
        ordering = ['-creado_el']

    def __str__(self):
        return self.tipo_vehiculo

class TipoPoliza(models.Model):
    
    cod_poliza = models.CharField(max_length=100, null=False,verbose_name="Código póliza")
    tipo_poliza = models.CharField(max_length=100, null=False,verbose_name="Tipo póliza")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Tipo de póliza'
        verbose_name_plural = 'Tipos de póliza'
        ordering = ['-creado_el']


    def __str__(self):
        return self.tipo_poliza

class TipoSiniestro(models.Model):
    
    cod_siniestro= models.CharField(max_length=100, null=False,verbose_name="Código siniestro")
    tipo_siniestro = models.CharField(max_length=100, null=False,verbose_name="Tipo siniestro")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Tipo Siniestro'
        verbose_name_plural = 'Tipos de siniestro'
        ordering = ['-creado_el']

    def __str__(self):
        return self.tipo_siniestro

class Marca(models.Model):

    cod_marca= models.CharField(max_length=100, null=False,verbose_name="Código marca")
    marca = models.CharField(max_length=100, null=False,verbose_name="Marca")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['marca']

    def __str__(self):
        return self.marca

class ModeloVehiculo(models.Model):
    marca_modelo = models.OneToOneField(Marca,null=False,on_delete= models.CASCADE)
    #tipo_modelo = models.OneToOneField(TipoVehiculo,null=False,on_delete= models.CASCADE)
    cod_modelo= models.CharField(max_length=100, null=False,verbose_name="Código modelo")
    modelo = models.CharField(max_length=100, null=False,verbose_name="Modelo vehículo")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Modelo vehículo'
        verbose_name_plural = 'Modelos de vehículo'
        ordering = ['modelo']

    def __str__(self):
        return self.modelo

class TablaSiniestros(models.Model):
    tipo_de_siniestro = models.OneToOneField(TipoSiniestro,null=False,on_delete=models.CASCADE,default="")
    tipo_de_poliza = models.OneToOneField(TipoPoliza,null=False,on_delete=models.CASCADE,default="")
    nombre_marca = models.OneToOneField(Marca,null=False,on_delete=models.CASCADE,default="")
    nombre_modelo = models.OneToOneField(ModeloVehiculo,null=False,on_delete=models.CASCADE,default="")
    tipo_de_vehiculo = models.OneToOneField(TipoVehiculo,null=False,on_delete=models.CASCADE,default="")
    nombre_conductor = models.CharField(max_length=100, null=False, verbose_name="Nombre conductor(a)")
    apellido_conductor =  models.CharField(max_length=100, null=False, verbose_name="Apellido conductor(a)")
    edad_conductor =  models.IntegerField(null=False, verbose_name="Edad conductor(a)",default="18")
    rut_conductor = models.CharField(max_length=100, null=False, verbose_name="Rut conductor(a)")
    fecha_siniestro =  models.DateField(null=False, verbose_name="Fecha siniestro")
    fecha_registro =  models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')
    descripcion_siniestro = models.TextField(max_length=300,null=False,verbose_name="Descripción siniestro")
    

    class Meta:
        verbose_name = 'Siniestro'
        verbose_name_plural = 'BD Siniestros'
        ordering = ['rut_conductor']

    def __str__(self):
        return self.rut_conductor

INGRESADO= 'Ingresado'
APROBADO = 'Aprobado'
EN_REPARACION = 'En reparación'
EN_ENTREGA = 'En entrega'
CERRADA = 'Cerrada'
INCIDENCIA = 'Incidencia'


ESTADO_CHOICES = (
    (INGRESADO,INGRESADO),
    (APROBADO,APROBADO),
    (EN_REPARACION,EN_REPARACION),
    (EN_ENTREGA,EN_ENTREGA),
    (CERRADA,CERRADA),
    (INCIDENCIA,INCIDENCIA),
)

class TablaDeSiniestros(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
        
    tipo_de_siniestro = models.ForeignKey(TipoSiniestro,blank=False,on_delete=models.CASCADE,verbose_name="Tipo de siniestro",default="")
    tipo_de_modelo = models.ForeignKey(ModeloVehiculo,blank=False,on_delete=models.CASCADE, verbose_name="Modelo vehículo",default="")
    nombre_marca = models.ForeignKey(Marca,blank=False,on_delete=models.CASCADE,verbose_name="Marca vehículo",default="")
    tipo_de_vehiculo = models.ForeignKey(TipoVehiculo,blank=False,on_delete=models.CASCADE,verbose_name="Tipo de vehículo",default="")

    nombre_conductor = models.CharField(max_length=100, blank=False, verbose_name="Nombre conductor(a)",default="")
    apellido_conductor =  models.CharField(max_length=100, blank=False, verbose_name="Apellido conductor(a)",default="")
    edad_conductor =  models.IntegerField(blank=False, verbose_name="Edad conductor(a)",default=18)
    rut_conductor = models.CharField(max_length=100, blank=False, verbose_name="Rut conductor(a)",default="")
    tipo_de_poliza = models.ForeignKey(TipoPoliza,blank=False,on_delete=models.CASCADE,verbose_name="Póliza contratada",default="")

    fecha_siniestro =  models.DateField(auto_now_add=False,auto_now=False, null=False, blank=False, verbose_name="Fecha siniestro",default=timezone.now)
    descripcion_siniestro = models.TextField(max_length=300,blank=False, null=False,verbose_name="Descripción siniestro",default="")
    
    fecha_registro =  models.DateTimeField(auto_now_add=True, verbose_name='Fecha registro')
    updated_at =  models.DateField(auto_now=True,verbose_name="Última actualización")
    estado_siniestro = models.CharField(max_length=50,choices=ESTADO_CHOICES,default=INGRESADO)
    

    class Meta:
        verbose_name = 'Ingreso de siniestro'
        verbose_name_plural = 'Ingreso de siniestros'
        
        #ordering = ['tipo_de_siniestro']

    def __str__(self):
        datos = f'{self.nombre_conductor} {self.apellido_conductor} / Rut {self.rut_conductor}'
        return datos

ADMIN = 'Administrador'
LIQUIDADOR = 'Liquidador'
CLIENTE = 'Cliente'

USUARIO_CHOICES = (
    (ADMIN,ADMIN),
    (LIQUIDADOR,LIQUIDADOR),
    (CLIENTE,CLIENTE),
)

class DataBaseUsuarios(models.Model):
    tipo_usuario = models.CharField(max_length=50,choices=USUARIO_CHOICES)
    nombre_usuario = models.CharField(max_length=50,blank=False,default='')
    apellido_usuario = models.CharField(max_length=50,blank=False,default='')
    cargo_usuario = models.CharField(max_length=50,blank=False,default='')
    mail_usuario = models.EmailField(max_length=100, default='@liquidaya.com')

    class Meta:
        ordering = ['tipo_usuario','apellido_usuario']
    
    def __str__(self):

        nombre_completo = f'{self.apellido_usuario}, {self.nombre_usuario} / {self.tipo_usuario} / {self.cargo_usuario}'
        return nombre_completo

    
class FormularioContacto(models.Model):
    nombre_contacto = models.CharField(max_length=100,verbose_name="Nombre")
    apellido_contacto = models.CharField(max_length=100,verbose_name="Apellido")
    email_contacto = models.EmailField(max_length=100,verbose_name="Email")
    texto_contacto = models.TextField(max_length=400,verbose_name="Mensaje")

    def __str__(self):

        return self.email_contacto