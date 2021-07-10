from .forms import StudentForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student


# def home(request):
#     return HttpResponse("This is home page")


def home_page(request):
    return render(request, "fscohort/home.html")


def student_list(request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm()
    context = {
        "form":form,
    }
    return render(request, "fscohort/student_add.html", context)