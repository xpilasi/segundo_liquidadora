from .models import TablaDeSiniestros
from django.views.generic.list import ListView

class ListaDeSiniestros(ListView):
    model = TablaDeSiniestros

  
     