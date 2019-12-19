from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def profile(request):
    return render(request, 'profile.html')
