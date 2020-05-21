from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)	
	lastName = models.CharField(max_length=50)
	type_user = models.IntegerField()

	def __str__(self):
		return self.username