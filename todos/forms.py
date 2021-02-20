from django import forms

class addForm(forms.Form):
    title = forms.CharField(required=True, max_length=100)
    description = forms.CharField(required=True, widget=forms.Textarea)
    is_completed = forms.BooleanField(required=False)