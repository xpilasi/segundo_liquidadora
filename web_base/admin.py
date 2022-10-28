from atexit import register
from web_base.models import Marca, TipoPoliza, TipoSiniestro, TipoVehiculo, ModeloVehiculo,TablaSiniestros,TablaDeSiniestros
from web_base.models import DataBaseUsuarios, FormularioContacto
from django.contrib import admin

# Register your models here.

admin.site.register(TipoVehiculo)
admin.site.register(TipoPoliza)
admin.site.register(TipoSiniestro)
admin.site.register(Marca)
admin.site.register(ModeloVehiculo)
admin.site.register(TablaSiniestros)

admin.site.register(DataBaseUsuarios)


        
admin.site.register(TablaDeSiniestros)
admin.site.register(FormularioContacto)

# class SiniestrosAdmin(admin.ModelAdmin):

