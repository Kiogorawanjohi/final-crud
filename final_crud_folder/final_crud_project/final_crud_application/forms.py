from django import forms
from .models import Registration
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['Names', 'Email', 'Phone', 'National_ID', 'County']