from django.shortcuts import render
from django.http import HttpResponse
def display(request):
	s="<h1>"+"welcome to the world of python web development"+"</h1>"
	return HttpResponse(s)
