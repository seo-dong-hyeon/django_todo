from django import forms

class addForm(forms.Form):
    title = forms.CharField(required=True, max_length=100)
    description = forms.CharField(widget=forms.Textarea)