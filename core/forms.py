from django import forms
from .models import Profile, Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label='Company Name')

    class Meta:
        model = User
        fields = ('first_name', 'email')


class ProfileForm(forms.ModelForm):
    phone = forms.IntegerField()
    gender = forms.RadioSelect()
    hobbies = forms.CharField()
    picture = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('phone', 'gender', 'hobbies', 'picture')


class AddProfileForm(forms.ModelForm):
    name = forms.CharField()
    type = forms.RadioSelect()
    email = forms.EmailField()

    class Meta:
        model = Company
        fields = ('type', 'email', 'name')
