from django.views.generic import View
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.core.context_processors import csrf
from .forms import UserForm

# Create your views here.

def home(request):
	return render(request, 'fosssite/home.html')
def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('fosssite/login.html',c)
	
def UserFormView(request):
	form_class=UserForm
	template_name='fosssite/signup.html'

	if request.method=='GET':
		form=form_class(None)
		return render(request,template_name,{'form':form})


		#validate by forms of django
	if request.method=='POST':
		form=form_class(request.POST)

		if form.is_valid():
			# not saving to database only creating object
			user=form.save(commit=False)
			#normalized data
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			#not as plain data
			user.set_password(password)
			user.save() #saved to database
			return render_to_response('fosssite/home.html',user)
		else:
			return render(request,template_name,{'form':form})

def auth_view(request):
	username=request.POST.get('username', '')
	password=request.POST.get('password', '')
	user=auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/loggedin')#url in brackets
	else:
		return HttpResponseRedirect('/invalid')

def loggedin(request):
	return render_to_response('fosssite/loggedin.html',{'fullname':request.user.username})

def logout(request):
	auth.logout(request)
	return render_to_response('fosssite/logout.html')

def invalid_login(request):
	return render_to_response('fosssite/invalid_login.html')
