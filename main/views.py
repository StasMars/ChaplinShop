from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Chaplin',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_auth': True

    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')


def prices(request):
    context = {
        'title': 'Prices',
        'content1': 'Авторизируйтесь, чтобы увидеть цены на продукты',
        'content2': 'Цены на продукты',
        'price1': 1000,
        'price2': 2000,
        'price3': 3000,
        'price4': 4000,
        'is_auth': True
    }

    return render(request, 'main/prices.html', context)