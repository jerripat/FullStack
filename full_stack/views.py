from django.shortcuts import render

def index(request):
    return render(request, 'full_stack/index.html')

def about(request):
    return render(request, 'full_stack/about.html')

def contact(request):
    return render(request, 'full_stack/contact.html')

