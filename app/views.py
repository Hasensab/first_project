from django.shortcuts import render
from django.http import *

# Create your views here.
def hasen(request):
    return HttpResponse('hai hasen how is ur software work')

def hai(request):
    return HttpResponse('<h1 style="color:red"><marquee>hey hasen welcome to webpage</h1></marquee>')
def macha(request):
    return render(request,'macha.html')