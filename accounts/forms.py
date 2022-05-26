from django import forms
from django.contrib.auth.models import User
from notice.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
        widgets = {
        
        'username': forms.TextInput(
        attrs={'style': 'text-align: center; width:220px; font-size:20px;', 'placeholder': 'Name'},
        ), 
        'password': forms.PasswordInput(
            attrs={'style': 'text-align: center; width:220px; font-size:20px;', 'placeholder': 'Password'}
        )} 

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = { 
        'username': forms.TextInput(
            attrs={'style': 'text-align: center; width: 220px; font-size:20px;'},
        ),
        'password': forms.PasswordInput(
            attrs={'style': 'text-align: center; width: 220px; font-size:20px;'}
        ) }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tag']

