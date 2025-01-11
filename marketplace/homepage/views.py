from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    return render(request, template, {})


def sign(request):
    template = 'homepage/sign-form.html'
    return render(request, template, {})
