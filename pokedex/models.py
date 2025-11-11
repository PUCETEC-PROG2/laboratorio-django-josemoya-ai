from django.db import models

### Entrenador
class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    level = models.IntegerField(default=1)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to='pokemons/', null=False, blank=True)

    def __str__(self):
        return self.name
