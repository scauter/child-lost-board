from django.contrib import admin
from .models import Room

@admin.register(Room)

class RoomNumberAdmin(admin.ModelAdmin):
	class Meta:
       		pass
