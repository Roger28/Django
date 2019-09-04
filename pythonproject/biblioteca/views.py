from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def biblioteca(request):
	return HttpResponse("testando a biblioteca")
