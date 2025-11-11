from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    picture = models.ImageField(upload_to='pokemons/', null=False, blank=True)

    def __str__(self):
        return self.name

### Entrenador
#class Trainer(models.Model):
    # Nombre
    # Apellido
    # Nivel
    # Fecha de nacimiento DateField()