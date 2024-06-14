




from django.urls import path
from . import views
from .views import listar_servicios

urlpatterns = [
	path('index',views.index, name='index'),
    path('servicios/', listar_servicios, name='listar_servicios'),
		]

