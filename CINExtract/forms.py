from django import forms

class CINForm(forms.Form):
    cin = forms.CharField(label='Corporate Identification Number', max_length=22)