# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from folhaponto.serializers import *

from folhaponto.models import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset =Frequencia.objects.all()
    serializer_class = FrequenciaSerializer
