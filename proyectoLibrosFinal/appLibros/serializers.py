from rest_framework import serializers
from appLibros.models import Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autor
        fields='__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields='__all__'