from django import db
from django.shortcuts import get_object_or_404, redirect, render
from events_app.forms import EventForm
from events_app.models import Category, Event

# Create your views here.
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_events(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)
    events = Event.objects.filter(category=category, is_approved=True)
    return render(request, 'category_events.html', {'category': category, 'events': events})

def event_list(request):
    events = Event.objects.filter(is_approved=True)
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    #event = Event.objects.get(id=event_id, is_approved=True)
    event =  get_object_or_404(Event, id=event_id, is_approved=True)
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', event_id = event.id)   
    else:
        form = EventForm()

    return render(request, 'event_create.html', {'form': form})

