from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as auth_messages

from .models import *
from .forms import *
from .utils import category_sort_key


def index(request):
    # query = request.GET.get('query', '')
    topic_id = int(request.GET.get('topic', '0'))
    topics = Topic.objects.all()
    topics = sorted(topics, key=category_sort_key)
    rooms = Room.objects.all()
    messages = Message.objects.all()
    if topic_id:
        rooms = rooms.filter(topic_id=topic_id)
    # if query:
    #     rooms = rooms.filter(name__icontains=query)
        
    context = {'topics': topics, 'rooms': rooms, 'messages': messages, 'topic_id': topic_id}
    return render(request, 'core/index.html', context)

def faq(request):
    context = {}
    return render(request, 'core/faq.html', context)

def contact(request):
    context = {}
    return render(request, 'core/contact.html', context)

def tos(request):
    context = {}
    return render(request, 'core/tos.html', context)

def about(request):
    context = {}
    return render(request, 'core/about.html', context)

def register(request):
    if request.method == str("POST"):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            auth_messages.success(request, 'Account created successfully!')
            
            return redirect('/')
    else:
        form = RegisterForm()
        
    context = {'form': form}
    return render(request, 'core/register.html', context)

@login_required
def inbox(request):
    topic_id = int(request.GET.get('topic', '0'))
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    messages = Message.objects.all()
    if topic_id:
        rooms = rooms.filter(topic_id=topic_id)
        
    context = {'topics': topics, 'rooms': rooms, 'messages': messages, 'topic_id': topic_id}
    return render(request, 'core/inbox.html', context)

@login_required
def add_room(request):
    if request.method == "POST":
        form = AddRoomForm(request.POST)
        
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user #Musi być zrobione w ten sposób
            room.save()
            auth_messages.success(request, 'Room created successfully!')
            
            return redirect('core:inbox')
    else: 
        form = AddRoomForm()
    
    context = {'form': form}
    return render(request, 'core/add_room.html', context)


@login_required    
def room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    messages = Message.objects.filter(room=room)
    
    if request.method == "POST":
        form = AddMessageForm(request.POST)
        
        if form.is_valid():
            msg = form.save(commit=False)
            msg.room = room
            msg.host = request.user #Musi być zrobione w ten sposób
            msg.save()
            auth_messages.success(request, 'Message created successfully!')
            
            return redirect('core:room', pk=pk)
    else: 
        form = AddMessageForm()
        
    context = {'room': room, 'messages': messages, 'form': form}
    return render(request, 'core/room.html', context)

@login_required
def mess(request, mess_pk):
    mess = get_object_or_404(Message, pk=mess_pk)
    
    context = {'mess': mess}
    return render(request, 'core/mess.html', context)

@login_required
def mess_delete(request, mess_pk):
    mess = get_object_or_404(Message, pk=mess_pk, host=request.user)
    mess.delete()    
    
    return redirect('core:index')

@login_required
def mess_edit(request, mess_pk):
    mess = get_object_or_404(Message, pk=mess_pk, host=request.user)
    
    if request.method == "POST":
        form = AddMessageForm(request.POST, instance=mess)
        
        if form.is_valid():
            form.save()
            
            return redirect('core:index')
    else: 
        form = AddMessageForm(instance=mess)
    
    context = {'form': form}
    return render(request, 'core/mess_edit.html', context)

@login_required
def delete(request, pk):
    room = get_object_or_404(Room, pk=pk, host=request.user)
    room.delete()    
    
    return redirect('core:index')
    
@login_required
def edit(request, pk):
    room = get_object_or_404(Room, pk=pk, host=request.user)
    
    if request.method == "POST":
        form = AddRoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            
            return redirect('core:index')
    else: 
        form = AddRoomForm(instance=room)
    
    context = {'form': form}
    return render(request, 'core/edit.html', context)