from django.shortcuts import render, redirect
from .models import ROOM, message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = ROOM.objects.get(name=room)
    return render(request, 'root.html',{
        'username':username,
        'room':room,
        'room_details':room_details
    })

def checkview(request,):
    room = request.POST['room_name']
    username = request.POST[ 'username' ]

    if ROOM.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = ROOM.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
        message = request.POST['message']
        username = request.POST['username']
        room_id= request.POST['room_id']

        new_message = message.objects.create(value=message, user=username,room=room_id)
        new_message.save()
        return HttpResponse('message sent sucessfully')

def getMessaages(request,room):
    room_details = ROOM.objectss.get(name=room)

    message = message.objects.filter(room =room_details.id)
    return JsonResponse({"messages":list(message.value())})
