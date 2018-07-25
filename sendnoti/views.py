from django.shortcuts import render
from pyfcm import FCMNotification
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .models import UserDetail,Message
from .serializers import UserdetailSerializer,MessageSerializer
from rest_framework.response import Response

push_service = FCMNotification(
    api_key="AAAA0ud_6ns:APA91bEHVPyl_lN9TDzZU-b3b1wewTpSPCvVXjjU2EAydj3Sptj8x2CoTXDbbqzBm5Kr-s0x7ISDzR97gtiWNkbcfghQpDZnnvOV-9CO7O383L3ZvBgLt23PndjZ_cFU--r0R64VWFsh")

def home(request):
    return render(request,'index.html',{})

def message(request):
    return render(request,'message.html',{})

class notify_user(APIView):
    def post(self,request,*args,**kwargs):
        message_title = request.data.get('notification_title')
        message_body = request.data.get('notification_body')
        selected_user=request.data.getlist("selected_user[]")
        print(selected_user)
        dev_ids=[]
        for users in selected_user:
            user=UserDetail.objects.get(id=users)
            if user.firebase_token != None:
                dev_ids.append(user.firebase_token)
        results = push_service.notify_multiple_devices(registration_ids=dev_ids, message_title=message_title,message_body=message_body)
        return JsonResponse({"message": "Task Completed."}, status=status.HTTP_200_OK)

class show_details(APIView):
    def post(self,request,*args,**kwargs):
        user_id = request.data.get('id')
        user=UserDetail.objects.get(id=user_id)
        return JsonResponse({"details":user.detail, "name":user.name, "phone":user.phone_number }, status=status.HTTP_200_OK)

class save_user(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserdetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class all_user(APIView):
    def get(self,request):
        user_all=UserDetail.objects.all()
        serializer = UserdetailSerializer(user_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
class save_message(APIView):
    def post(self,request):
        phone=request.data.get("phone_number")
        msg=request.data.get("message")
        try:
            user=UserDetail.objects.get(phone_number=phone)
            Message.objects.create(user=user,message=msg)
            return Response({"message":"Message is saved."},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":"Phone number is wrong.","error":e},status=status.HTTP_400_BAD_REQUEST) 


class all_message(APIView):
    def get(self,request):
        message_all=Message.objects.all().order_by('-pk')
        serializer = MessageSerializer(message_all,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

