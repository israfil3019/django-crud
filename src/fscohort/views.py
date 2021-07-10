from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse("This is home page")


def home_page(request):
    return render(request, "fscohort/home.html")
