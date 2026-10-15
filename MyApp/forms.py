
from django import forms
from .models import Reminder


class ReminderForm(forms.ModelForm):

    class Meta:
        model = Reminder

        fields = [
            'item_name',
            'category',
            'date',
            'time',
            'status',
            'notes'
        ]

        widgets = {
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name'
            }),

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),

            'status': forms.Select(attrs={
                'class': 'form-control'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your notes here...'
            }),
        }
