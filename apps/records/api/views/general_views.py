from rest_framework import viewsets
from apps.records.api.serializers import RecordSerializer
from rest_framework.response import Response
from rest_framework import status
from apps.records.models import Record
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class RecordViewSet (viewsets.ViewSet) :
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request) :
        records = Record.objects.all()
        serializer = self.serializer_class(records, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None) :
        record = get_object_or_404(Record, pk=pk)
        serializer = self.serializer_class(record)
        
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request) :
        data = request.data
        serializer = self.serializer_class(data=data)

        if (serializer.is_valid()) :
            serializer.save()
            return Response({
                'message': 'The new record was created correctly',
                'record': serializer.data,
            },status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None) :
        record = get_object_or_404(Record, pk=pk)
        serializer = self.serializer_class(record, data=request.data)

        if (serializer.is_valid()) :
            serializer.save()
            return Response({
                'message': 'The record was rightfully updated',
                'record': serializer.data,
            }, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None) :
        record = get_object_or_404(Record, pk=pk)
        record.delete()
        return Response({
            'message': 'The record was deleted successfully',
        }, status=status.HTTP_200_OK)