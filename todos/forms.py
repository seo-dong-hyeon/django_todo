from django import forms
from todos.models import Todo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_completed')

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                'title', 'description', 'is_completed',
                ButtonHolder(
                        Submit('create', 'Create', css_class='btn btn-primary')
                )
        )