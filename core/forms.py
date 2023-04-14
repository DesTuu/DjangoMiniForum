from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


CLS = "w-full py-4 px-6 rounded-xl"
CLS2 = "w-full py-4 px-6 rounded-xl border-8"

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': CLS
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': CLS
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': CLS
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Reapeat password',
        'class': CLS
    }))
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': CLS
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': CLS
    }))
    
class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('topic', 'name', 'description')
        widgets = {
            'topic': forms.Select(attrs={
                'class': CLS2
            }),
            'name': forms.TextInput(attrs={
                'class': CLS2
            }),
            'description': forms.Textarea(attrs={
                'class': CLS2
            })
        }
        
class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': CLS2
            }),
        }
        
# class EditMessageForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('name', 'description', 'price', 'image', 'is_sold')
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': CLS2
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': CLS2
#             }),
#             'price': forms.TextInput(attrs={
#                 'class': CLS2
#             }),
#         }