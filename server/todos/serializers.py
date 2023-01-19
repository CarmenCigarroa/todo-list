from rest_framework.serializers import ModelSerializer
from .models import *

class TodoListSerializer(ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'