from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Tarefas
from .serializers import TarefasSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_list(request):
    tarefas = tarefas.objects.filter(user=request.user)
    
    status_filter = request.query_params.get('completed')
    if status_filter is not None:
        tarefas = tarefas.filter(completed=status_filter.lower() == 'true')

    paginator = PageNumberPagination()
    paginated_tarefas = paginator.paginate_queryset(tarefas, request)
    serializer = TarefasSerializer(paginated_tarefas, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def task_create(request):
    serializer = TarefasSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, id):
    tarefas = get_object_or_404(tarefas, id=id, user=request.user)
    
    if request.method == 'GET':
        serializer = TarefasSerializer(tarefas)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TarefasSerializer(tarefas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tarefas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
