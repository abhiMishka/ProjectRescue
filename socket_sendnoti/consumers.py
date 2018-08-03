from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class NotifyConsumer(WebsocketConsumer):

    def connect(self):
        print("harsj")
        self.room_name = self.scope['url_route']['kwargs']['phone_number']
        self.room_group_name = 'notify_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        phone_list = text_data_json['phone_list']
        message=text_data_json['message']
        title=text_data_json['title']
        for number in phone_list:
            print( self.room_group_name)
            async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'send_message_user',
                        'message': message,
                        'title':title,
                    }
                )

    def send_message_user(self, event):
        print("here")
        message = event['message']
        title = event['title']
        self.send(text_data=json.dumps({
            'message': message,
            'title':title,
        }))


