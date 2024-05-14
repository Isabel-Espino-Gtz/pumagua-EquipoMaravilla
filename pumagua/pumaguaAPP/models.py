from django.db import models

# Create your models here.
class bebederos(models.Model):
    estados = (
    ('0', 'No disponible'),
    ('1', 'Disponible'),
    ('2', 'En mantenimiento'),
    )

    estado_bebedero = models.CharField(default='1',help_text="EstadoBebeder", max_length=1, choices=estados)
    id_bebedero = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length = 100, blank = True)
    institucion = models.CharField(max_length = 100, blank = True)
    palabras_clave = models.CharField(max_length = 500, blank = True)
    descripcion = models.CharField(max_length = 1000, blank = True, default = '')
    latitud = models.FloatField(max_length = 100, blank = True, default = None, null = True)
    longitud = models.FloatField(max_length = 100, blank = True, default = None, null = True)

    def __str__(self):
        return f'Nombre: {self.nombre} Ubicacion: {self.ubicacion}'

class Reporte(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    bebedero = models.ForeignKey(bebederos, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()  # Añadido para describir el reporte
    dato_extra = models.CharField(max_length=255, blank=True, null=True)  # Campo opcional para información adicional

    def __str__(self):
        info_extra = f' - {self.dato_extra}' if self.dato_extra else ''
        return f'Reporte de {self.bebedero.nombre} - {self.descripcion}{info_extra}, hecho por {self.nombre} ({self.email}) en {self.fecha_reporte.strftime("%Y-%m-%d %H:%M")}'