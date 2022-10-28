from gc import get_objects
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistroSiniestro
from .models import ModeloVehiculo, TablaDeSiniestros,TipoPoliza,TipoSiniestro,TipoVehiculo,Marca
from .models import DataBaseUsuarios, FormularioContacto
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
import csv
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import FormContacto


# Create your views here.

#@login_required(login_url="")
def index(request):

    form_contacto = FormContacto()

    if request.method == 'POST':
        form_contacto = FormContacto(request.POST)

        if form_contacto.is_valid():
            form_contacto.save()
            #messages.success(request,'Te has registrado correctamente')

            return redirect('index')

    return render(request,'index.html',{
        'title':'Inicio',
        'form_contacto': form_contacto,
    }
    )


class IngresoSiniestroCreateView(LoginRequiredMixin,CreateView):
    model = TablaDeSiniestros
    template_name = 'web_base/registro_siniestro.html'
    fields = [
    'tipo_de_siniestro',
    'tipo_de_modelo',
    'tipo_de_modelo',
    'nombre_marca',
    'tipo_de_vehiculo',
    'nombre_conductor',
    'apellido_conductor',
    'edad_conductor',
    'rut_conductor',
    'tipo_de_poliza',
    'fecha_siniestro',
    'descripcion_siniestro',
    
    ] 
    
    success_url = reverse_lazy('registro_exitoso')

    def form_valid(self,form): #método para que se asigne el usuario automáticamente al logeado
        form.instance.usuario = self.request.user
        return super(IngresoSiniestroCreateView,self).form_valid(form)

@login_required(login_url="")
def registro_exitoso(request):

    if request.method == 'POST':

        return redirect('index')

    return render(request,'registro_exitoso.html',{
        'title':'Registro exitoso',
    }
    )

def formulario_enviado(request):

    if request.method == 'POST':

        return redirect('index')

    return render(request,'formulario_enviado.html',{
        'title':'Formulario enviado',
    }
    )

@login_required(login_url="")
def mantencion_datos(request):
    return render(request,'mantencion_datos.html',{
        'title':'Mantención de datos',

    })
@login_required(login_url="")
def exportar(request):
    return render(request,'exportar.html',{
        'title': 'Exportar BD',
    })

class SiniestrosListView(LoginRequiredMixin,ListView):

    model = TablaDeSiniestros
    context_object_name= 'siniestros'
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['siniestros'] = context['siniestros'].filter(usuario=self.request.user) #filtra las tareas del usuario que está logeado en el momento
        
        valor_buscado_1 = self.request.GET.get('buscar_por_id') or ''

        if valor_buscado_1:
            context['siniestros'] = context['siniestros'].filter(id__icontains= valor_buscado_1)
        
            context['valor_buscado_1'] = valor_buscado_1
        
        valor_buscado_2 = self.request.GET.get('buscar_por_rut') or ''

        if valor_buscado_2:
            context['siniestros'] = context['siniestros'].filter(rut_conductor__icontains= valor_buscado_2)
        
            context['valor_buscado_2'] = valor_buscado_2
    
        return context        

# Login

class LogIn(LoginView):
    template_name = 'web_base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['title'] = 'Prueba'
        return context


#Editar BD:

class EditarSiniestro(UpdateView):
    model = TipoSiniestro
    fields = ['tipo_siniestro']
    success_url = reverse_lazy('editar_tipo_siniestro')

class EditarTipoVehiculo(UpdateView):
    model = TipoVehiculo
    fields = ['tipo_vehiculo']
    success_url = reverse_lazy('editar_tipo_vehiculo')

class EditarMarca(UpdateView):
    model = Marca
    fields = ['marca']
    success_url = reverse_lazy('editar_marca')

class EditarModelo(UpdateView):
    model = ModeloVehiculo
    fields = ['modelo']
    success_url = reverse_lazy('editar_modelo')

class EditarPolizas(UpdateView):
    model = TipoPoliza
    fields = ['tipo_poliza']
    success_url = reverse_lazy('editar_polizas')

class EditarEstado(UpdateView):
    model = TablaDeSiniestros
    fields = ['estado_siniestro',]
    success_url = reverse_lazy('siniestros')
    context_object_name= 'siniestros'

#Listas:

class PolizasListView(ListView):

    model = TipoPoliza
    context_object_name= 'polizas'

    class Meta:
        ordering = ['-cod_poliza']
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['polizas'] = context['polizas'] #filtra las tareas del usuario que está logeado en el momento
    
        return context  

class TipoSiniestroListView(ListView):

    model = TipoSiniestro
    context_object_name= 'tipo_siniestros'

    class Meta:
        ordering = ['tipo_siniestros']
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['tipo_siniestros'] = context['tipo_siniestros'] #filtra las tareas del usuario que está logeado en el momento
    
        return context  

class TipoVehiculoListView(ListView):

    model = TipoVehiculo
    context_object_name= 'tipo_vehiculos'

    class Meta:
        ordering = ['tipo_vehiculos']
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['tipo_vehiculos'] = context['tipo_vehiculos'] #filtra las tareas del usuario que está logeado en el momento
    
        return context  

class MarcaListView(ListView):

    model = Marca
    context_object_name= 'marca'

    class Meta:
        ordering = ['marca']
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['marca'] = context['marca'] #filtra las tareas del usuario que está logeado en el momento
    
        return context  

class ModeloListView(ListView):

    model = ModeloVehiculo
    context_object_name= 'modelo'

    class Meta:
        ordering = ['modelo']
    
    def get_context_data(self,**kwarg):
        context = super().get_context_data(**kwarg)
        context['modelo'] = context['modelo'] #filtra las tareas del usuario que está logeado en el momento
    
        return context 

# class IngresarSiniestro(LoginRequiredMixin,CreateView):
#     model = RegistroSiniestro
#     fields = '__all__'
#     success_url = reverse_lazy('registro_exitoso')

#     def form_valid(self,form): #método para que se asigne el usuario automáticamente al logeado
#         form.instance.usuario = self.request.user
#         return super(IngresarSiniestro,self).form_valid(form)

# Exportar a CSV:

def exportar_usuarios(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Tipo usuario','Nombre','Apellido','Cargo','Mail'])

    for base in DataBaseUsuarios.objects.all().values_list('tipo_usuario','nombre_usuario','apellido_usuario','cargo_usuario','mail_usuario'):
        writer.writerow(base)
        
    response['Content-Disposition'] = 'attachment; filename="db_usuarios_2.csv"'
    return response

def exportar_siniestros(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([
        'Id#',
        'Tipo sin',
        'Fecha sin',
        'Fecha reg',
        'Poliza',
        'Vehiculo',
        'Marca',
        'Modelo',
        'Rut c',
        'Nombre c',
        'Apellido c',
        'Edad c',
        'Estado sin'])

    for base in TablaDeSiniestros.objects.all().values_list(
        'id',
        'tipo_de_siniestro',
        'fecha_siniestro',
        'fecha_registro',
        'tipo_de_poliza',
        'tipo_de_vehiculo',
        'nombre_marca',
        'tipo_de_modelo',
        'rut_conductor',
        'nombre_conductor',
        'apellido_conductor',
        'edad_conductor',
        'estado_siniestro'
        ):
        
        writer.writerow(base)
        
    response['Content-Disposition'] = 'attachment; filename="db_siniestros_total.csv"'
    return response

# Vista detallada

class SiniestroDetailView(DetailView):
    model = TablaDeSiniestros
    context_object_name = 'detalle_siniestro'

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'web_base/user_detail.html'
    context_object_name = 'user'

# class IngresoFormulario(CreateView):
#     model = FormularioContacto
#     template_name = 'index.html'
#     fields = '__all__'
#     success_url = reverse_lazy('formulario_enviado')

    

        
        


