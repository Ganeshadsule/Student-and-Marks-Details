from django import forms
from form_app.models import Student
class StudentForm(forms.Form):
    name = forms.CharField(
        label='Student Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
        })
    )

    mark = forms.IntegerField(  
        label='Student Mark',
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your mark',
        })
    )
