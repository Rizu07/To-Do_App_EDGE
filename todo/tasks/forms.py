from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter task title...'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter task description...', 'rows': 3}), required=False)
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
