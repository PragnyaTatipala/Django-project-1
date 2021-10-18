#from django.db.models import fields
from rest_framework import serializers
from . models import timediff

class timediffSerializer(serializers.ModelSerializer):

    class Meta:
        model=timediff
        #fields=('start_time','end_time')
        fields='__all__'
