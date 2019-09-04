from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context = {'secret_key': settings.SECRET_KEY},)
