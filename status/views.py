from status.models import Status
from .serializer import status_serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import generics


# Create your views here.
class Statusapi(APIView):
    def get(self, request, format=None):
        status_list = Status.objects.all()
        serializer_list = status_serializer(status_list, many=True)
        return Response(serializer_list.data)

class Statuslist(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = status_serializer

class StatusCreateapi(generics.CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = status_serializer

class StatusDetailsApi(generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = status_serializer

class StatusUpdateApi(generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = status_serializer

class StatusDeleteApi(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = status_serializer






