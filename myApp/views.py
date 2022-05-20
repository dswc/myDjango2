from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def sayhello(request):
    return HttpResponse('sayhello.......')

def hello2(request, username):
    now = datetime.now()
    return render(request, 'hello3.html', {'username':username, 'now':now})
