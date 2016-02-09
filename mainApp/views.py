from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.

#lists the entire directory, by default shows the home directory
def showDir(request, path=""):
	x = os.path.join(settings.BASE_DIR, 'static')
	
	#create the full path and scan the entire directory
	fullPath = x + '/'+ path
	r, d, f = scanDir(fullPath)
	
	#creates paths inside the home directory
	d = joinPaths(path, d)
	f = joinPaths(path, f)

	return render(request, "home.html", {'r':r, 'd':d, 'f':f, 'path':path})

#for joining the paths with the previous ones
def joinPaths(prev, a):
	if prev == "":
		return a
	l = list()
	for x in a:
		l.append(prev + '/' + x)
	return l

#used for scanning the present directory
def scanDir(path):
	count = 1;
	root, dirs, files = list(), list(), list()

	# break os.walk after one iteration
	for r, d, f in os.walk(path):		
		dirs = d
		files = f
		root = r
		break

	return root, dirs, files
