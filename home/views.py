from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def home(request):
	data = {}
	return render(request,'home/base.html', data)

def about(request):
	# return HttpResponse('<h1>Blog About 2</h1>')
	posts = [
	    {
	        'author': 'CoreyMS',
	        'title': 'Blog Post 1',
	        'content': 'First post content',
	        'date_posted': 'August 27, 2018'
	    },
	    {
	        'author': 'Jane Doe',
	        'title': 'Blog Post 2',
	        'content': 'Second post content',
	        'date_posted': 'August 28, 2018'
	    }
	]
	context = {
        'posts': posts,
        'title': "hello"
    }
	return render(request,'home/home.html',context)
