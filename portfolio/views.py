from django.shortcuts import render
from .models import Home, Touch, Project
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
                                                    


def home_list(request):
    home = Home.objects.all()
    touch = Touch.objects.all()
    project = Project.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            send_mail(subject,
                        message, from_email, 
                        ['sylarnano688@gmail.com'])
            try:
                send_mail(subject, 
                            message,
                            from_email,
                            ['sylarnano688@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect( 'portfolio:home_list')

    return render(request, 'portfolio/base.html', {'form': form, 
                                                    'home':home, 
                                                    'touch':touch,
                                                    'project':project})
                                                    
