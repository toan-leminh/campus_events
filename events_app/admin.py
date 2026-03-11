from django.contrib import admin

from events_app.models import Category, Event

# Admin class
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'start_datetime', 'end_datetime', 'location', 'is_approved']
    list_filter = ('is_approved',)
    search_fields = ['title', 'description', 'location', 'contact_name', 'contact_email']

class CategoryAdmin(admin.ModelAdmin):    
    list_display = ['name', 'description']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)