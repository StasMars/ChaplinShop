from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Chaplin - Главная',
        'content': 'Chaplin'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Chaplin - О нас',
        'content': 'О нас',
        'text_on_page': 'Магазин одежды в стиле фильмов с Чарли Чаплином. Enjoy.'
    }

    return render(request, 'main/about.html', context)


