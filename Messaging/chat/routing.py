# chat/routing.py
from django.urls import path 

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<slug:room_name>/',consumers.chatConsumer)
]