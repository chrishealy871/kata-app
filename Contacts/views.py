from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts_list.html", {'contacts': contacts})


def contact_details(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact.save()
    return render(request, 'contacts_details.html', {'contact': contact})

def new_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect(contact_details, contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contactform.html', {'form': form})



def edit_contact(request, id):
    post = get_object_or_404(Contact, pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            contacts = form.save(commit=False)
            contacts.save()
            return redirect(contact_details, contact.pk)
    else:
        form = ContactForm(instance=post)
    return render(request, 'contactform.html', {'form': form})
