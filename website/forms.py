from django import forms
from django.forms import ModelForm, fields
from .models import User
from django.contrib.auth.hashers import make_password

# instantiating from forms.form custom Class
# class NameForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Your Name')
#     def save(self):
#         pass

# instantiating from modelForm class, that has built-in methods and funcs
class UserForm(ModelForm):
    class Meta:
        model = User
        # fields = ['username', 'password']
        fields = '__all__'

#overriding save method to hash the password
    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m