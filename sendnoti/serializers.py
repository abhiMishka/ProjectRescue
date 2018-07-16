from rest_framework import serializers
from .models import UserDetail

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserDetail
        fields = '__all__'