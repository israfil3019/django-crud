from django.views.generic.base import TemplateView
from .forms import StudentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from django.views.generic import TemplateView,  ListView


# def home(request):
#     return HttpResponse("This is home page")


def home_page(request):
    return render(request, "fscohort/home.html")


class HomeView(TemplateView):
    template_name = "fscohort/home.html"


def student_list(request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(request, "fscohort/student_list.html", context)


class StudentList(ListView):
    model = Student
    # template_name           # default app/student_list.html == we dont have to write this. 
    context_object_name = "students"    # default object list


def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        'form': form,
    }
    return render(request, "fscohort/student_add.html", context)


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        "student": student
    }
    return render(request, "fscohort/student_detail.html", context)


# def student_update(request, id):
    # student = get_object_or_404(Student, id=id)
    # form = StudentForm(instance=student)
    # if request.method == "POST":
    #     form = StudentForm(request.POST, instance=student)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("list")

    # context = {
    #     "student" : student,
    #     "form" : form
    # }

    # return render(request, "fscohort/student_update.html", context)


def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    # student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('list')

    context = {
        "student": student,
        "form": form
    }

    return render(request, "fscohort/student_update.html", context)


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('list')

    context = {
        "student": student
    }

    return render(request, "fscohort/student_delete.html", context)