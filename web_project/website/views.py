# Create your views here.
from django.shortcuts import render


def add(request):
  return render(request, 'website/add.html')
