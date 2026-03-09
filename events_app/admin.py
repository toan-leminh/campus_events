from django.contrib import admin

from events_app.models import Category, Event

# Admin class
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'start_datetime', 'end_datetime', 'is_approved']
    list_filter = ('is_approved',)
    search_fields = ['is_approved', 'category']

# Register your models here.
admin.site.register(Category)
admin.site.register(Event, EventAdmin)