from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'done']


class ContactForm(forms.Form):
    Full_name = forms.CharField(max_length=50, min_length=4,
                                widget=forms.TextInput(
                                    attrs={
                                        "class": "form-control",
                                        "placeholder": "First Name Last Name"
                                    }
                                ))
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }
        )
    )
    # Enrollment = forms.IntegerField()
    Gender = forms.ChoiceField(choices=[('male', 'MALE'), ('female', 'FEMALE')])
    Message = forms.CharField(max_length=150, min_length=4,
                                widget=forms.Textarea(
                                    attrs={
                                        "class": "form-control",
                                        "placeholder": "Your Message"
                                    }
                                ))
