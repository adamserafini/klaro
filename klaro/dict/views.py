

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'dict/index.html')


def search(request):
    return render(request, 'dict/results.html')
