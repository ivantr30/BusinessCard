from .models import ApplicationModel
from django import forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'nameInputField'}),
            'email' : forms.TextInput(attrs={'class' : 'emailInputField'}),
            'offer' : forms.Textarea(attrs={'class' : 'offerInputField'}),
        }