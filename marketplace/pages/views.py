from django.shortcuts import render


def marketplace(request):
    template = 'pages/marketplace.html'
    return render(request, template, {})


def rankings(request):
    template = 'pages/rankings.html'
    return render(request, template, {})


def connect_a_wallet(request):
    template = 'pages/connect_a_wallet.html'
    return render(request, template, {})
