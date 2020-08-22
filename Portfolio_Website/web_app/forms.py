from django import forms
from web_app.models import Employer

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Employer
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Full Name'}),
            'company' : forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Company'}),
            'position' : forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Position'}),
            'email' : forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Email'}),
            'message' : forms.Textarea(attrs = {'class':'form-control', 'placeholder': "Let's Connect"}),
        }