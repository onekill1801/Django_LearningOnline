from django.db import models

# Create your models here.
class Courser(models.Model):
	nameCourser = models.CharField(max_length=200)
	starCourser = models.CharField(max_length=50)
	imageCourser = models.ImageField()
	
class LearningOutcomes(models.Model):
	id_user = models.IntegerField()
	id_courser = models.IntegerField()
	output = models.CharField(max_length=200)

class ContentCourser(models.Model):
	id_courser = models.IntegerField()
	content = models.CharField(max_length=2000)
	nameContent = models.CharField(max_length=200)

		