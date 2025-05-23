from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'category', 'description', 'status', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('user__username', 'category', 'description')
