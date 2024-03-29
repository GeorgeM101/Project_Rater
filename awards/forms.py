from django import forms
from .models import Profile, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project,Profile,Rating

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','email']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields =['design', 'usability', 'content'] 

