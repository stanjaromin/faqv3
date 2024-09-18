# forms.py

from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter question'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter answer', 'rows': 4}),
        }
