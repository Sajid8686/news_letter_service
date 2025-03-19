from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter_dashboard, name='dashboard'),
    path('index/', views.index, name='index'),
    path('unsubscribe/<int:sub_id>/', views.unsubscribe, name='unsubscribe'),
    path('newsletter/', views.newsletter, name='newsletter'),
    
]