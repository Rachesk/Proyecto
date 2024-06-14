from django.shortcuts import render
from .models import Servicio
# Create your views here.



def index(request):
	context={}
	return render(request,'servicios/index.html',context)



def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/listar_servicios.html', {'servicios': servicios})