from django.urls import path
from . import views

urlpatterns = [
    path('reminders/', views.reminder_list, name='reminder_list'),
    path('reminders/add/', views.add_reminder, name='add_reminder'),
    path('reminders/edit/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),
    path('reminders/delete/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
]
