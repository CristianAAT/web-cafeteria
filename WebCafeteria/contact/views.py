from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def Contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y direccionamos
            email = EmailMessage(
                "Cafeteria: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contesta@inbox.mailtrap.io",
                ["Cristian_AAT@outlook.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('Contact')+'?ok')
            except:
                return redirect(reverse('Contact')+'?fail')

    return render(request, "contact/contact.html", {'form':contact_form})