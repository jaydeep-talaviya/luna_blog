from django.urls import path


from .views import createRoom, room,AllRoom


urlpatterns = [
    path('room/', createRoom, name="createRoom"),
    path('room/all/', AllRoom, name="AllRoom"),
    path('room/<str:name>/', room, name="room"),

]
