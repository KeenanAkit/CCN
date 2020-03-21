from rest_framework import serializers
from .models import Ccna

class CcnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ccna
        fields = ('id', 'name', 'email', 'message')
