from __future__ import unicode_literals
from django.db import models
import bcrypt



# Create your models here.
class UserManager(models.Manager):
	def register_user(self, postData):
		errors = []

		if len(postData['name']) < 3:
			errors.append('Name must be at least 3 characters long.')

		if len(postData['username']) < 3:
			errors.append('Username must be at least 3 characters long.')

		if len(postData['password']) < 8:
			errors.append('Password name must be at least 8 characters long.')

		if not postData['password'] == postData['password_confirmation']:
			errors.append('Password fields must match.')

		if self.filter(username = postData['username']):
			errors.append('Please enter a username.')

		response_to_views = {}

		if not errors:
			hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = self.create(name = postData['name'], username = postData['username'], password = hashed_password)
			response_to_views['user'] = user
			response_to_views['status'] = True

		else:
			response_to_views['errors'] = errors
			response_to_views['status'] = False

		return response_to_views


	def login_user(self, postData):
		user = self.filter(username = postData['username'])
		response_to_views = {}
		
		if not user:
			response_to_views['status'] = False
			response_to_views['errors'] = 'Username found.'

		else:
			if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
				response_to_views['status'] = True
				response_to_views['user'] = user[0]
				response_to_views['welcome'] = "Successfully logged in."

			else:
				response_to_views['status'] = False
				response_to_views['errors'] = 'Invalid username and/or password.'

		return response_to_views



class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()