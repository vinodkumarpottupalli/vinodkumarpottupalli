from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class NewJobPostForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'min_salary','max_salary','desc','type','location']

        labels = {
            'title': 'Job Title',
            'min_salary': 'Min Salary',
            'max_salary': 'Max Salary',
            'type': 'Type',
            'desc': 'Job Description',
            'location': 'Location'
        }

    def __init__(self, *args, **kwargs):
        super(NewJobPostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'type': 'text'})
        self.fields['title'].widget.attrs.update({'id': 'jt'})

class NewJobForm(forms.Form):
    title = forms.CharField(label='Job Title', max_length=100)
    min_salary = forms.CharField(label='Min Salary', max_length=15)
    max_salary = forms.CharField(label='Min Salary', max_length=15)
