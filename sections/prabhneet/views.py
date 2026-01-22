from django.shortcuts import render

def home(request):
    return render(request, 'prabhneet/home.html')