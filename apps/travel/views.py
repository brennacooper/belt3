from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from .models import Destination
from ..loginreg.models import User

# Create your views here.
def index(request):
	
	context = {
	"destinations": Destination.objects.all(),
		
	}

	return render(request, "travel/index.html", context)

def show(request, id):
	context = {
	"destinations": Destination.objects.all(),
		
	}
	return render(request, "travel/destination.html", context)

def join(request):
	pass

def add_travel(request):
	return render (request, "travel/add.html")

def add(request):
	
	response_from_models = Destination.objects.add_new_destination(request.POST)
	print "-" * 50

	if response_from_models ['status']:

		return redirect('travel:index')

	else:
		messages.error(request, response_from_models['errors'])
		return redirect('travel:add_travel')


	