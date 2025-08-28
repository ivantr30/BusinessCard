from .models import ApplicationModel
from django import forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'nameInputField', 'placeholder' : 'Enter your name'}),
            'email' : forms.TextInput(attrs={'class' : 'emailInputField', 'placeholder' : 'Enter your email'}),
            'offer' : forms.Textarea(attrs={'class' : 'offerInputField', 'placeholder' : 'Enter your offer'}),
        }