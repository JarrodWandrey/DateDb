from django import forms
from .models import Date

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['name', 'location', 'date', 'rating', 'price']
