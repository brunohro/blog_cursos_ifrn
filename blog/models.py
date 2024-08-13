from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True, blank=True)

    def __str__(self):
        return self.nome
