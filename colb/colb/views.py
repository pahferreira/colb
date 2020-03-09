from django.shortcuts import render, redirect

def index(request):
    user_agent = request.META.get("HTTP_USER_AGENT")
    mobile_os = ["android", "iphone", "ipad"]

    if any(mobile in user_agent.lower() for mobile in mobile_os):
        return redirect('https://m.colb.global')

    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')