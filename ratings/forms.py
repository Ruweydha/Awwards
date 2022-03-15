from pyexpat import model
from django import forms
from .models import Profile, Project, Ratings

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['project', 'user', 'average']
