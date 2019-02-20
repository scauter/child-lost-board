from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django_filters.views import FilterView

from django.shortcuts import render, get_object_or_404, redirect

from logging import getLogger

from django.shortcuts import render

#from .filters import ItemFilterSet

from .models import LostChildInfo
from .models import Room
import random


def index(request):
    if request.method == 'POST':
        room_num = request.POST.getlist('room_num') 
        request.session['room_num'] = room_num
        return HttpResponseRedirect("./info")
        
    room_all = []
    for obj in Room.objects.all():
        room_all.append(obj.num)
    return render(request, 'app/index.html', {'room_all': room_all})

def create(request):
    room_num = random.randrange(10**7, 10**8)
    room = Room(num=room_num)
    room.save()
    content = '部屋番号が発行されました。\n' + str(room_num)
    return render(request, 'app/display_roomnum.html', {
        'text': content
        })


def info_list(request):
    
    room_num = int((request.session['room_num'])[0])
    room = Room.objects.get(num=room_num)
    info_list_queryset = LostChildInfo.objects.filter(room=room)

    
    if request.method == 'POST':
        input_info = request.POST.getlist('lost_child_info') 
        lost_child_info = LostChildInfo(room=room, content=input_info[0])
        lost_child_info.save()

    info_list = info_list_queryset
        
    return render(request, 'app/info_list.html', {'info_list': info_list})

def info_edit(request, info_id=None):
    if info_id:   # info_id が指定されている (修正時)
        info = get_object_or_404(LostChildInfo, id=info_id)

    if request.method == 'POST':
        input_info = request.POST.getlist('edit_info')
        LostChildInfo.objects.filter(id=info_id).update(content=input_info[0])
        
        return HttpResponseRedirect("../")

    return render(request, 'app/info_edit.html', {'info':info})

def info_del(request, info_id):
    info = get_object_or_404(LostChildInfo, id=info_id)
    info.delete()
    return HttpResponseRedirect("../")
