from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Chat,Room


class RoomSerializer(ModelSerializer):
    total_user = SerializerMethodField("get_total_users")
    last_message = SerializerMethodField("get_last_message")

    class Meta:
        model = Room
        fields = ['name','description','creater','room_profile','total_user','last_message']

    def get_total_users(self, obj):
        try:
            return obj.room.values('user').distinct().count()
        except Exception as e:
            return 0
    
    def get_last_message(self,obj):
        try:
            return obj.room.last().message
        except Exception as e:
            return '' 

class ChatSerializer(ModelSerializer):
    user = SerializerMethodField("get_name")
    user_id = SerializerMethodField("get_user_id")

    class Meta:
        model = Chat
        fields = '__all__'

    def get_name(self, obj):
        return obj.user.username
    def get_user_id(self, obj):
        return obj.user.id