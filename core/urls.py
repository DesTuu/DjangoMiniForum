from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('tos/', views.tos, name='tos'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('inbox/', views.inbox, name='inbox'),
    path('add_room/', views.add_room, name='add_room'),
    path('room/<int:pk>/', views.room, name='room'),
    path('mess/<int:mess_pk>/', views.mess, name='mess'),
    path('mess/<int:mess_pk>/mess_delete/', views.mess_delete, name='mess_delete'),
    path('mess/<int:mess_pk>/mess_edit/', views.mess_edit, name='mess_edit'),
    path('room/<int:pk>/delete/', views.delete, name='delete'),
    path('room/<int:pk>/edit/', views.edit, name='edit'),
]
