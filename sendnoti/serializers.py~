from rest_framework import serializers
from .models import UserDetail,Message

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = UserDetail
        fields = '__all__'
        
class MessageSerializer(serializers.ModelSerializer):
    name=serializers.ReadOnlyField(source='user.name',read_only=True)
    phone_number=serializers.ReadOnlyField(source='user.phone_number',read_only=True)
    class Meta(object):
        model = Message
        fields = ('name','phone_number','message')
