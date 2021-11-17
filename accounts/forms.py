from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account
from django import forms

class AccountUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email',)


class AccountUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email',)
