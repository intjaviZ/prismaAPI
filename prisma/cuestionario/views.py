from rest_framework import generics, status
from .models import GradoEscolar, Pregunta, EscalaValoracion, Alumno, Evaluacion, Resultado
from .serializers import GradoEscolarSerializer, PreguntasSerializer, EscalaValoracionSerializer

from collections import defaultdict
from rest_framework.response import Response

from rest_framework.decorators import api_view
from django.db import transaction

# Create your views here.
# Vista para listar y crear grados escolares
class GradoEscolarListCreateView(generics.ListCreateAPIView):
    queryset = GradoEscolar.objects.all()
    serializer_class = GradoEscolarSerializer

class PreguntasView(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntasSerializer

# class EscalaValoracionView(generics.ListCreateAPIView):
#     queryset = EscalaValoracion.objects.all()
#     serializer_class = EscalaValoracionSerializer
class EscalaValoracionView(generics.ListAPIView):
    queryset = EscalaValoracion.objects.all()
    serializer_class = EscalaValoracionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = self.get_serializer(queryset, many=True).data

        # Agrupar por id_dimension
        grouped_data = defaultdict(list)
        for item in serialized_data:
            grouped_data[item["id_dimension"]].append(item)

        return Response(list(grouped_data.values()))

@api_view(['POST'])
def guardar_resultado(request):
    data = request.data
    nombre = data.get('nombre')
    grado = data.get('grado')
    puntos = data.get('puntos')
    extra = data.get('extra','')
    
    if not nombre or grado is None or puntos is None:
        return Response({"error": "Faltan datos obligatorios."}, status=status.HTTP_400_BAD_REQUEST)
    
    with transaction.atomic():
        alumno = Alumno.objects.create(nombre=nombre, grado_escolar=grado)
        print(f"alumno: {alumno}")
        print(f"puntos: {puntos}")

        evaluacion = Evaluacion.objects.filter(min_valor__lte=puntos, max_valor__gte=puntos).first()
        print(f"evaluacion: {evaluacion}")
        if not evaluacion:
            return Response({"error": "No se encontró una evaluación para los puntos dados."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        resultado = Resultado.objects.create(id_alumno=alumno,
                                             id_evaluacion=evaluacion,
                                             puntos=puntos,
                                             extra=extra)
        
        return Response({
            "id_resultado": resultado.id_resultado,
            "id_alumno": alumno.id_alumno,
            "evaluacion": evaluacion.evaluacion,
            "puntos": resultado.puntos
        }, status=status.HTTP_201_CREATED)
