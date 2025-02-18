# urls.py
from django.urls import path
from .views import GradoEscolarListCreateView, PreguntasView, EscalaValoracionView, guardar_resultado

urlpatterns = [
    path('grados/', GradoEscolarListCreateView.as_view(), name='grado-escolar-list'),
    path('preguntas/', PreguntasView.as_view(), name='preguntas-lis'),
    path('escalaValoracion/', EscalaValoracionView.as_view(), name='escalaValoracion-list'),
    path('guardarTest/', guardar_resultado, name='registrar')

]
