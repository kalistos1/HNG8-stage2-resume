from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method=='POST':
       form = ContactForm(request.POST)

       if form.is_valid():
           info = form.cleaned_data

           #get form data
           get_name = info['name']
           get_email=info['email']
           get_subject=info['subject']
           get_message=info['message']

           # save form
           form.save()

           #send mail
           email_subject = f'New contact {get_email}: {get_subject}'
           email_message = get_message
           send_mail(email_subject, email_message,'', ['ucktech1@gmail.com'])

           print(get_name)
           return redirect ('successPage')

       else:
            messages.success(request,'please make sure no field is empty')
            return redirect('index')
    else:  
        form=ContactForm()      
        context = {
                'form':form
                }
        return render(request,'home/index.html', context)

def successPage(request):
    return render(request, 'success.html')