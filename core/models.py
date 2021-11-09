from django.db import models

class Boletim(models.Model):
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2)
    nota4 = models.DecimalField(max_digits=4, decimal_places=2)
