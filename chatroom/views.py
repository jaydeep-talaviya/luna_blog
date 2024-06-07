from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import JsonResponse
from django.contrib.auth.models import User

import json


from .models import Chat, Room
from .serializers import ChatSerializer,RoomSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRoom(request):
    if request.method == "POST":
        data = json.loads(request.body)
        existed_room = Room.objects.filter(name = data['name'])
        if existed_room:
            room = Room.objects.create(name = data['name'], description = data['description'],creater=request.user)
            serializer = RoomSerializer(room)
            return JsonResponse({"status": 201,'room':serializer.data})
        else:
            return JsonResponse({"status": 400,'message':'Room Already Existed!'})

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def room(request, name):
    if request.method == "GET":
        room = Room.objects.get(name=name)
        messages = reversed(room.room.all())
        serializer = ChatSerializer(messages, many=True)
        return Response(serializer.data)

    if request.method == "DELETE":
        room = Room.objects.get(name=name)
        if room.creater_id == request.user.id:
            room.delete()
            return JsonResponse({"status": 200,'message':"Room has been Removed Successfully"})
        else:
            return JsonResponse({"status": 400,'message':"You can not remove This Room!"})
        

    if request.method == "POST":
        print(request.POST, request.data, sep="\n")
        room = Room.objects.get(name=name)
        user = request.user
        try:
            message = request.data.get('message')
        except:
            message = ""
        try:
            image = request.data.get('image')
            print(image)
            if image == "undefined":
                image = None
        except:
            image = None
        chat = Chat.objects.create(user=user, room=room, message=message, image=image)
        chat.save()
        # chat = ChatSerializer(data=request)
        # chat.user = user
        # chat.room = room
        # if chat.is_valid():
        #     chat.save()
        return JsonResponse({"status": "201"})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def AllRoom(request):
    print(">>>>>>step 1")
    rooms=Room.objects.all()
    print(">>>>>>>>",rooms)
    serializer = RoomSerializer(rooms,context={"request": request}, many=True)
    return Response(serializer.data)
