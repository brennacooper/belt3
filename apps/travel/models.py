from __future__ import unicode_literals
from datetime import date
from django.db import models
from ..loginreg.models import User

# Create your models here.
class UserManager(models.Manager):
	def add_new_destination(self, postData):
		errors = []

		if len(postData['name']) < 1:
			errors.append('Destination cannot be empty.')

		if len(postData['description']) < 1:
			errors.append('Description cannot be empty.')

		if date(postData['date_from']) < date.today():
			errors.append('Date cannot be in the past.')

		if date(postData['date_to']) < date.today():
			errors.append('Date cannot be in the past.')

		response_to_views = {}

		if not errors:
			destination = self.create(name=request.POST['name'], description=request.POST['description'], date_from=request.POST['date_from'], date_to=request.POST['date_to'])
			response_to_views['destination'] = destination
			response_to_views['status'] = True

		else:
			response_to_views['errors'] = errors
			response_to_views['status'] = False

		return response_to_views

class Destination(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(max_length=1000)
	date_from = models.DateTimeField(null=True)
	date_to = models.DateTimeField(null=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ManyToManyField(User, related_name="destinations")

	objects = UserManager()