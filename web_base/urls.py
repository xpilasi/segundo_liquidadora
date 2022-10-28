from django.urls import path
from . import views
from .views import IngresoSiniestroCreateView, SiniestrosListView,PolizasListView,TipoSiniestroListView,TipoVehiculoListView,MarcaListView,ModeloListView
from .views import EditarSiniestro,EditarTipoVehiculo,EditarMarca,EditarModelo,EditarPolizas, EditarEstado
from .views import SiniestroDetailView,LogoutView
from .views import LogIn, UserDetailView #IngresoFormulario
# from .views import IngresarSiniestro



urlpatterns = [
    path('',views.index,name='index'),

    # Login
    path('accounts/login/',LogIn.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),

    # Perfil usuario
    path('mi_perfil/<int:pk>/',UserDetailView.as_view(), name='mi_perfil'),

    # Registro siniestro (con forms)
    path('registro_siniestro/',IngresoSiniestroCreateView.as_view(),name='registro'),
    path('registro_exitoso/',views.registro_exitoso,name='registro_exitoso'),

    # Mantencion de datos base (render)
    path('mantencion_datos/',views.mantencion_datos,name='mantencion'),
    
    # Estado siniestros
    path('siniestros/',SiniestrosListView.as_view(),name='siniestros'),
    #   Editar
    path('siniestros/editar_estado/<int:pk>/',EditarEstado.as_view(),name='editar_estado'),
    #   Ver
    path('siniestros/<int:pk>/',SiniestroDetailView.as_view(),name='detalle_estado'),
    
    #URL mantención pólizas
    path('polizas/',PolizasListView.as_view(),name='editar_polizas'),
    path('polizas/<int:pk>',EditarPolizas.as_view(),name='tipo_polizas'),
    
    #URL mantención siniestros
    path('editar_siniestros/',TipoSiniestroListView.as_view(),name='editar_tipo_siniestro'),
    path('editar_siniestros/<int:pk>',EditarSiniestro.as_view(),name='tipo_siniestros'),

    #URL mantención tipo vehículos
    path('editar_vehiculos/',TipoVehiculoListView.as_view(),name='editar_tipo_vehiculo'),
    path('editar_vehiculos/<int:pk>',EditarTipoVehiculo.as_view(),name='tipo_vehiculo'),

    #URL mantención tipo marcas
    path('editar_marca/',MarcaListView.as_view(),name='editar_marca'),
    path('editar_marca/<int:pk>',EditarMarca.as_view(),name='marca'),

    #URL mantención modelos
    path('editar_modelo/',ModeloListView.as_view(),name='editar_modelo'),
    path('editar_modelo/<int:pk>',EditarModelo.as_view(),name='modelo'),

    path('exportar/',views.exportar,name='exportar'),
    #Exportar CSV usuarios
    path('siniestros/exportar_usuarios/',views.exportar_usuarios,name='exportar_db_usuarios'),
    #Exportar CSV siniestros
    path('siniestros/exportar_siniestros/',views.exportar_siniestros,name='exportar_db_siniestros'),

    #Formulario contactos
    #path('#contacto/',IngresoFormulario.as_view(),name='formulario_contacto'),
    path('formulario_enviado/',views.formulario_enviado,name='formulario_enviado'),


]