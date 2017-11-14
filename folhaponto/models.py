from django.db import models
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    sexo = models.CharField(max_length=1)
    idade = models.IntegerField()
    usuario = models.ForeignKey(User, null=True, blank=False)
    def __str__(self):
        return '{}'.format(self.nome)
class Horario(models.Model):
	dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)
	dataEHoraDeFim = models.DateTimeField(blank=True, null=True)
	tipo = models.BooleanField("Estagiario",default=True)
	ip = models.CharField(max_length=128)
	nomechefe = models.CharField(max_length=128)
	def __str__(self):
		 return '{}'.format(self.nomechefe)
class Frequencia(models.Model):
	funcionario = models.ForeignKey(Funcionario, related_name = 'funcionario_dados', null = True, blank = False)
	horario = models.ForeignKey(Horario, related_name = 'horario_funcionario', null = True, blank = False)
	status = models.BooleanField("CONSISTENTE",default=True)
	justificativa = models.TextField()
	def __str__(self):
		return '{}'.format(self.funcionario)

