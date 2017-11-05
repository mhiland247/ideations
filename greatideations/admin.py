from django.contrib import admin
from .models import ContactEntry
from django.core import serializers
from django.http import HttpResponse
from django.db.models.loading import get_model

# Register your models here.
class ContactEntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': [ 'message']}),
        ('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),
    ]

    list_display = ( 'message',)
    list_filter = ['created_date']
    search_fields = ['message']

# Register your models here.

admin.site.register(ContactEntry, ContactEntryAdmin)
