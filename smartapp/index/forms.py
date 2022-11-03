from django import forms
from django.contrib.auth.forms import UserCreationForm


class TextArea(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, "placeholder": "Enter your text here"}), label='')


class Response(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label='')
