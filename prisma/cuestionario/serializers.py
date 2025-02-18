# serializers.py
from rest_framework import serializers
from .models import GradoEscolar, Pregunta, EscalaValoracion

class GradoEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradoEscolar
        fields = ['id_grado', 'grado']  # Campos que serán expuestos en el API

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = ['id_pregunta', 'pregunta', 'id_dimension']

class EscalaValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalaValoracion
        fields = ['id_escala_valoracion', 'escala_valoracion', 'valor', 'id_dimension']