from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    if request.method == 'POST':
        person = request.POST['person']
        return HttpResponse(person)
    if request.method == 'GET':
        person = request.GET['person']
        return HttpResponse(person)
