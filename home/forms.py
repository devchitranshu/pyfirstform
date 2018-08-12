from django import forms

from .models import FirstForm

class FirstForm(forms.ModelForm):

    class Meta:
        model = FirstForm
        fields = ('csv','title', 'text',)