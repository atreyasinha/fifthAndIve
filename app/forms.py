from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Customer

class RegistrationForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'street_address', 'apt_house', 'city', 'state', 'zipcode', 'phone_number']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstName', 'placeholder': 'John'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastName', 'placeholder': 'Doe'}),
                   'street_address': forms.TextInput(attrs={'class': 'form-control', 'id': 'street_address', 'placeholder': '1234 Main St'}),
                   'apt_house': forms.TextInput(attrs={'class': 'form-control', 'id': 'apt_house', 'placeholder': 'Apartment or suite'}),
                   'city': forms.TextInput(attrs={'class': 'form-control', 'id': 'city', 'placeholder': 'Albany'}),
                   'state': forms.Select(attrs={'class': 'form-select', 'id': 'state'}),
                   'zipcode': forms.NumberInput(attrs={'class': 'form-control', 'id': 'zip', 'placeholder': '12009'}),
                   'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'id': 'phoneNumber', 'placeholder': '(999)-999-9999'})}
