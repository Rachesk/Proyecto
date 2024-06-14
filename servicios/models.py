from django.db import models

# Create your models here.




class Servicio(models.Model):
    id               = models.CharField(primary_key=True, max_length=10)
    precio           = models.DecimalField(max_digits=10, decimal_places=2)
    foto             = models.ImageField(upload_to='fotos_servicios/')
    descripcion      = models.TextField()

    def __str__(self):
        return f'Servicio {self.id} - {self.descripcion[:20]}'   
