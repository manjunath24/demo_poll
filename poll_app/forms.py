from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())



class Profile(forms.Form):
    first_name = forms.CharField(required=False, help_text="Please enter minimun 6 characters")
    last_name = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    password_confirm = forms.CharField(label="Repeat Password", widget=forms.PasswordInput(), required=False, help_text="Please enter same password again")

    def clean(self):
		if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
		    password = self.cleaned_data['password']
		    password_confirm = self.cleaned_data['password_confirm']
		    if password != password_confirm:
		        raise forms.ValidationError("Two password didn't match")
		if 'first_name' in self.cleaned_data:
			first_name = self.cleaned_data['first_name']
			if len(first_name) < 6:
				raise forms.ValidationError('First Name should be of minimun 6 characters')
		return self.cleaned_data