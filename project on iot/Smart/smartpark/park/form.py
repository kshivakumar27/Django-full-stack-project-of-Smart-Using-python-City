from django import forms
from .models import *
from django.contrib.auth.models import User



# feedback form
class FeedbackForm(forms.Form):
    u_name = forms.CharField(required=True)
    u_email = forms.EmailField(required=True)
    u_phone = forms.CharField(required=True)
    u_rate = forms.CharField(required=True)
    u_suggestion = forms.CharField(required=True)
    u_review = forms.CharField(required=True)
    content = forms.CharField(required=True)