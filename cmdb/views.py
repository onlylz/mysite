from django.shortcuts import render
from django.shortcuts import HttpResponse
def index(request):
    #return HttpResponse("hello world!")
    return render(request, "index.html",)
# Create your views here.
