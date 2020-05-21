from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateCourserForm
from django.views.generic.base import View

data = {}

class MyCourserView(View):
	def get(self, request):
		return render(request,'mycoursers.html', data)
	def post(self, request):
		return render(request,'mycoursers.html', data)

class AllCourserView(View):
	def get(self, request):
		return render(request,'allcoursers.html', data)
	def post(self, request):
		return render(request,'allcoursers.html', data)