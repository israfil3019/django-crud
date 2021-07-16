from .forms import StudentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from django.views.generic import TemplateView,  ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


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
    # ordering = [nums]
    paginate_by = 2


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

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_add.html"  # app/student_form.html  == suffix  '_form'
    success_url = reverse_lazy('list')  # redirect == '/list/'


def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        "student": student
    }
    return render(request, "fscohort/student_detail.html", context)


class StudentDetail(DetailView):
    model = Student
    # pk_url_kwarg = 'id'  # from detail.py we can use id instead of pk
    # template_name = 


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
        messages.success(request, "Student succesfully updated.")
        return redirect('list')

    context = {
        "student": student,
        "form": form
    }

    return render(request, "fscohort/student_update.html", context)


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_update.html"  # app/student_form.html  == suffix  '_form'
    # success_url = reverse_lazy('list')
    success_url = '/list/'
    pk_url_kwarg = 'id'


def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect('list')

    context = {
        "student": student
    }

    return render(request, "fscohort/student_delete.html", context)


class StudentDelete(DeleteView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_delete.html"  # app/student_confirm_delete.html 
    success_url = reverse_lazy('list')
    # success_url = '/list/'
    pk_url_kwarg = 'id'