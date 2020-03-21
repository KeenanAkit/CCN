from django.shortcuts import render

# Create your views here.
from .models import Ccna
from .serializers import CcnaSerializer
from rest_framework import generics

class CcnaListCreate(generics.ListCreateAPIView):
    queryset = Ccna.objects.all()
    serializer_class = CcnaSerializer
 
