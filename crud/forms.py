from django import forms
from django.forms import ModelForm
from .models import surveyData

class surveyForm(forms.ModelForm):
    class Meta:
        model = surveyData
        fields = '__all__'