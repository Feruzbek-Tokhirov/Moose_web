from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):

    return render(request, "index-2.html")


def about(request):
    return render(request, "about.html")


def article(request):
    return render(request, "blog.html")


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(".")
    contex = {
        "form": form
    }
    return render(request, "contact.html", contex)
