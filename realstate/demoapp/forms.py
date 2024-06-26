from django import forms
from .models import PropertyInformation

class PropertyInformationForm(forms.ModelForm):
    class Meta:
        model = PropertyInformation
        fields = ['property_type', 'location', 'price']
