from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Главная страница приложения women")


def categories(request):
    return HttpResponse("<h1>Категории</h1>")
