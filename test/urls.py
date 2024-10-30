from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]