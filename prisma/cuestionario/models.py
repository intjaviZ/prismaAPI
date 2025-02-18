from django.db import models

class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)  # Llave primaria
    nombre = models.CharField(max_length=150)  # Limitamos a 150 caracteres
    grado_escolar = models.IntegerField()  # Referencia al id de grados_escolares
    fecha_realizacion = models.DateField(auto_now_add=True)  # Fecha con valor por defecto

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_alumno})"
    
    class Meta:
        db_table = 'alumnos'

class Dimension(models.Model):
    id_dimension = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    dimension = models.CharField(max_length=40)  # Limitar a 40 caracteres

    def __str__(self):
        return self.dimension
    
    class Meta:
        db_table = 'dimensiones'

class EscalaValoracion(models.Model):
    id_escala_valoracion = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    escala_valoracion = models.CharField(max_length=30)  # Limitar a 30 caracteres
    valor = models.IntegerField()  # Campo entero para el valor asociado
    id_dimension = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.escala_valoracion} (Valor: {self.valor})"
    
    class Meta:
        db_table = 'escalas_valoracion'

class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    evaluacion = models.CharField(max_length=50)  # Limitar a 50 caracteres
    min_valor = models.IntegerField()  # Campo para el valor mínimo
    max_valor = models.IntegerField()  # Campo para el valor máximo

    def __str__(self):
        return f"{self.evaluacion} ({self.min_valor} - {self.max_valor})"
    class Meta:
        db_table = "evaluaciones"

class GradoEscolar(models.Model):
    id_grado = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    grado = models.CharField(max_length=50)  # Limitar a 50 caracteres

    def __str__(self):
        return self.grado
    class Meta:
        db_table = 'grados_escolares'
    
class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    pregunta = models.CharField(max_length=100)  # Limitar a 100 caracteres
    id_dimension = models.IntegerField(null=True)

    def __str__(self):
        return self.pregunta
    
    class Meta:
        db_table = 'preguntas'
    
class Resultado(models.Model):
    id_resultado = models.AutoField(primary_key=True)  # Llave primaria autoincremental
    id_alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE, db_column='id_alumno') 
    id_evaluacion = models.ForeignKey('Evaluacion', on_delete=models.CASCADE, db_column='id_evaluacion')  # Relación con Evaluacion
    puntos = models.IntegerField()  # Campo para los puntos obtenidos
    extra = models.CharField(max_length=150, default='')

    def __str__(self):
        return f"Resultado {self.id_resultado} - Alumno: {self.id_alumno.nombre}, Evaluación: {self.id_evaluacion.evaluacion}, Puntos: {self.puntos}"
    
    class Meta:
        db_table = 'resultados'