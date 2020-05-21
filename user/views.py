from django.shortcuts import render
# from django.http import Http404
from django.http import HttpResponse
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm
import pdb
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

data = {}

@csrf_exempt
def login(request):
	# pdb.set_trace()
	if request.method == "POST":
		form = LoginForm(request.POST)
	if form.is_valid():
		user = auth.authenticate(
			username=form.cleaned_data["username"],
			password=form.cleaned_data["password"])
		# auth.login(request, user)
		return HttpResponseRedirect("/")
	else:
		form = LoginForm()
	# return HttpResponseRedirect("/")
	return render(request, 'profile.html', {'form':form})


class LoginView(View):
	def get(self, request):
		# pdb.set_trace()
		return render(request,'profile.html', data)

	# @csrf_protect
	@csrf_exempt
	def post(self, request):
		pdb.set_trace()
		if request.method == "POST":
			form = LoginForm(request.POST)
		if form.is_valid():
			user = auth.authenticate(
				username=form.cleaned_data["username"],
				password=form.cleaned_data["password"])
			return HttpResponseRedirect("/")
		else:
			return render(request,'profile.html', data)
		# login_form = LoginForm(request.POST)
		# if login_form.is_valid():
		# 	user_name = request.POST.get('username', '')
		# 	pass_word = request.POST.get('password', '')
		# 	return render(request,'profile.html', data)
		# return render(request,'profile.html', data)

class RegisterView(View):
	def get(self, request):
		return render(request,'register.html', data)
	def post(self, request):
		return render(request,'register.html', data)
