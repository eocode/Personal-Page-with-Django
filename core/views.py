from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def abilities(request):
    return render(request, "core/abilities.html")


def store(request):
    return render(request, "core/store.html")


def blog(request):
    return render(request, "core/blog.html")


def contact(request):
    return render(request, "core/contact.html")
