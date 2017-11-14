from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from folhaponto.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    	class Meta:
		model = User
		fields = ('url', 'username', 'email')
	def create(self, validated_data):
		user = User.objects.create(**validated_data)# pega todos objetos de usuario
		return user#Sempre deve retorna
			

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
	usuario = UserSerializer(many=False)
	class Meta:
		model = Funcionario
		fields = ('usuario','nome', 'sexo', 'idade')
	def create(self,dados):
		dados_user=dados.pop('usuario')# remove usuario
		u = User.objects.create(**dados_user)# criar o usuario
		p = Funcionario.objects.create(usuario=u,**dados)#criar pessoa, e em dados insere objetivo de usuario
		return p
class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    	class Meta:
		model = Horario
		fields = '__all__'
	def create(self, dados):
		dados_horas = Horario.objects.create(**dados)
		return dados_horas
class FrequenciaSerializer(serializers.HyperlinkedModelSerializer):
	funcionarios=FuncionarioSerializer(many=False)
	horario=HorarioSerializer(many=False)
	class Meta:
    		model = Frequencia
	fields = '__all__'
	def create(self,dados):
		dados_funcionarios=dados.pop('funcionario')
		dados_horario=dados.pop('horario')
		funcionarios=Funcionario.objects.create(**dados_funcionarios)
		horario=Horario.objects.create(**dados_horario)
		I = Frequencia.objects.create(funcionarios=funcionarios , horario=horario,**dados)
		return I