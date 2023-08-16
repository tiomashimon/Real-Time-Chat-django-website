from django.shortcuts import render
from .models import ChatRoom, ChatMessage


def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {'chatrooms': chat_rooms})


def chatroom(request, slug):
    chat_room = ChatRoom.objects.get(slug=slug)
    return render(request, 'chatapp/room.html', {'chatroom': chat_room})
