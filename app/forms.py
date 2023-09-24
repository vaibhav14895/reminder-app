from django import forms
from .models import *

class addtaskss(forms.ModelForm):
    
    class Meta:
        model = tasks
        fields = ("__all__")
