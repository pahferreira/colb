from django.shortcuts import render

def index(request):
    print(request)
    return render(request, 'index.html')