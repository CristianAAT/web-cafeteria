from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request, "core/home.html")

def About(request):
    return render(request, "core/about.html")

def Store(request):
    return render(request, "core/store.html")