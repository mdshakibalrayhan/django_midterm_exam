from django import forms
from .models import CarOwner

class CarOwnerForm(forms.ModelForm):
    class Meta:
        model = CarOwner
        fields = ['owned_car']