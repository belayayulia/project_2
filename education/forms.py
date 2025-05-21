from django import forms
from .models import EducationProgram

class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationProgram
        fields = '__all__'
        widgets = {
            'created_at': forms.HiddenInput(),
        }