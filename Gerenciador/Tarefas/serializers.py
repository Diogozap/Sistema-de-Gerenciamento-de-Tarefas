from rest_framework import serializers
from .models import Tarefas

class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']
