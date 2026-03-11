from django.urls import include, path

from events_app import views

urlpatterns = [
    path('', views.event_list, name='home'),

    path('category_list/', views.category_list, name='category_list'),
    path('category_events/<int:category_id>/', views.category_events, name='category_events'),

    path('event_list/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/create/', views.event_create, name='event_create'),
]