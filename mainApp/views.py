from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.

def home(request):
	x = os.path.join(settings.BASE_DIR, 'static')
	a = os.listdir(x)
	
	return render(request, "base.html", {'l':a})