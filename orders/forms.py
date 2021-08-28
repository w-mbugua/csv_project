from django import forms

from .models import Data

class DataModelForm(forms.ModelForm):
  class Meta:
    model = Data
    fields = ('file_name',)