# Create your views here.
from django.shortcuts import render
from django.template import RequestContext

def add(request):
  rc = RequestContext(request,{})
  return render(request, 'website/add.html',rc)
