from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generatePassword=''
    length=int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!#$%&/(=?')
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    for char in range(length):
        generatePassword+=random.choice(characters)
    return render(request,'password.html',{'password':generatePassword})
