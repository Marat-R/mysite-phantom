from django.forms import ModelForm
from .models import ContactData


class ContactData(forms.Form):
    name = forms.CharField