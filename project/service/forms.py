from django import forms
from .models import service,customer

class servicefrom(forms.ModelForm):
    class Meta:
      model=service
      fields='__all__'
      widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'desc1':forms.Textarea(attrs={'class':'form-control'}),
        'desc2':forms.Textarea(attrs={'class':'form-control'}),
        'img':forms.FileInput(attrs={'class':'form-control'}),
      }

class customerfrom(forms.ModelForm):
    class Meta:
      model=customer
      fields='__all__'
      widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'text':forms.Textarea(attrs={'class':'form-control'}),
        'img':forms.FileInput(attrs={'class':'form-control'}),
      }      