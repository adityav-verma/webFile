from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	username = request.user.username
	pathToHome = os.path.join(os.path.join(settings.BASE_DIR, 'static'), 'home')
	pathToUserHome = os.path.join(pathToHome, username)
	l = os.listdir(pathToHome)
	if username in l:
		return showDir(request, "")
	else:
		setupHomeDir(pathToUserHome)
		return showDir(request, "")

#setting up home directory, making all necessary folders like documents, photos, etc
def setupHomeDir(path):
	os.mkdir(path)		#making home
	dirsToMake = ['Documents', 'Music', 'Pictures', 'Videos']		#add trash feature
	for x in dirsToMake:
		os.mkdir(os.path.join(path, x))

#lists the entire directory, by default shows the home directory
@login_required
def showDir(request, path=""):
	x = os.path.join(os.path.join(os.path.join(settings.BASE_DIR, 'static'), 'home'), request.user.username)
	
	#create the full path and scan the entire directory
	absolutePath = x + '/'+ path
	r, d, f = scanDir(absolutePath)
	d.sort()
	f.sort()
	
	#creates paths inside the home directory
	d = joinPaths(path, d)
	f = joinPaths(path, f)

	temp = path.split("/")

	return render(request, "home.html", {'r':r, 'd':d, 'f':f, 'parentPath':path, 'temp':temp})


#create a new folder in the specified location
def createFolder(request):
	folderName = request.POST.get('folderName')
	folderPath = request.POST.get('folderPath')

	username = request.user.username
	x = os.path.join(os.path.join(os.path.join(settings.BASE_DIR, 'static'), 'home'), request.user.username)
	path = os.path.join(x, folderPath)
	os.mkdir(os.path.join(path, folderName))
	return showDir(request, folderPath)

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
