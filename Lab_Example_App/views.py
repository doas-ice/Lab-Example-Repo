from django.shortcuts import render, redirect, HttpResponse
from Lab_Example_App.models import Contact

def index(request):
    return render(request,'index.html')

def contacts(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        return HttpResponse('<h1>Thanks for contacting with us</h1>')
    return render(request, 'contacts.html')

def contact_req(request):
	contact = Contact.objects.all()
	context = {'contact':contact}
	return render(request, 'contact-requests.html', context)