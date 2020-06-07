from django import forms
from .models import Users, Desc
from django.forms import ModelForm

class PatchCard(ModelForm):
    class Meta:
        model = Desc
        fields = ['title', 'description', 'date',]
        exclude = ['user']


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ['name','username', 'password', 'email']
        exclude = ['date_joined']

class LoginForm(forms.Form):
    my_username = forms.CharField(label='username', max_length=20)
    my_password = forms.CharField(label='password', max_length=20, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        name = cleaned_data.get('my_username')
        pin = cleaned_data.get('my_password')

        try:
            p = Users.objects.get(username = name)
            try:
                q = Users.objects.get(password = pin)
                if p!=q:
                    raise forms.ValidationError('Password dont match')
            except Users.DoesNotExist:
                raise forms.ValidationError('Password incorrect')
        except Users.DoesNotExist:
            raise forms.ValidationError('User Does not exist')

