from rest_framework import serializers
from .models import*

class ec2s3Serilizer(serializers.ModelSerializer):
    class Meta:
        model = Ec2Service   
        fields = '__all__'