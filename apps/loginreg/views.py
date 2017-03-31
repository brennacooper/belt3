from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render (request, 'loginreg/index.html')

def register(request):
	response_from_models = User.objects.register_user(request.POST)
	print "-" * 50

	if response_from_models ['status']:
		request.session ['user_name'] = response_from_models['user'].name

		return redirect('travel:index')

	else:
		for error in response_from_models['errors']:
			messages.error(request, error)

		return redirect('login:index')

def login(request):
	response_from_models = User.objects.login_user(request.POST)
	print "-" * 50

	if response_from_models ['status']:
		request.session ['user_name'] = response_from_models['user'].name

		return redirect('travel:index')

	else:
		messages.error(request, response_from_models['errors'])
		return redirect('login:index')


def success(request):


	if not 'user_first_name' in request.session:
		messages.error(request, 'Must be logged in!')
		return redirect('login:index')

	return render(request, 'travel:index')
	

		

def logout(request):
	request.session.clear()
	return redirect('login:index')
