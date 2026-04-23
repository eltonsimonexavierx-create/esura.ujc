from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPOS = (
        ('ADMIN', 'Administrador'),
        ('PROF', 'Professor'),
        ('ESTUDANTE', 'Estudante'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo = models.CharField(max_length=10, choices=TIPOS, default='ESTUDANTE')

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"


