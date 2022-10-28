from django.forms import ModelForm
from .models import TablaDeSiniestros,FormularioContacto
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistroSiniestro(ModelForm):
    
    class Meta:
        model = TablaDeSiniestros
        exclude = ('usuario',)

class FormContacto(ModelForm):
    
    class Meta:
        model = FormularioContacto
        fields = '__all__'
        
        

        

        

    
    