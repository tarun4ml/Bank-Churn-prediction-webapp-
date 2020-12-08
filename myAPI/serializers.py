from rest_framework import serializers
from . models import exited

class exitedSerializers(serializers.ModelSerializer):
    class Meta:
        model= exited
        fields='__all__'