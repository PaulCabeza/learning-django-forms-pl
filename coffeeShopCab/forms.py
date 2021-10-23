from django import forms
from django.forms import ModelForm, fields
from .models import User

class NameForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    def save(self):
        pass

class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = ['username', 'password']
        fields = '__all__'