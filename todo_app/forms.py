from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={
                'class': 'input-form',
                'placeholder': 'Add a new todo...'
            })
        }
