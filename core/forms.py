from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]

    def __init__(self, *args, **kwargs):	    
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control', 'id':'name', 'placeholder':'Name'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control', 'id':'email', 'placeholder':'Email'})
        self.fields['subject'].widget.attrs.update({'class' : 'form-control', 'id':'subject', 'placeholder':'Subject'})
        self.fields['message'].widget.attrs.update({'class' : 'form-control', 'id':'message', 'placeholder':'Message'})
 
 