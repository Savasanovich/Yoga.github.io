from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request , 'index.html' , {})


def about_us(request):

    return render(request, 'about-us.html',{})


def blog(request):


    return render(request, 'blog.html',{})

def contact(request):

    return render(request, 'contact.html', {})

def classes(request):

    return render(request, 'classes.html', {})

def elements(request):

    return render(request, 'elements.html', {})