from django.shortcuts import render


def hello_world(request):
    return render(request, "home.html")


def subpage(request):
    return render(request, "subpage.html")
