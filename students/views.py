from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Students
from .forms import StudentForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='user_login')
def home(request):
    return render(request, 'students/index.html', {'students':Students.objects.all()})

@login_required(login_url='user_login')
def view_student(request,id):
    student = Students.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))

@login_required(login_url='user_login')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_age = form.cleaned_data['age']
            new_address = form.cleaned_data['address']
            new_grade= form.cleaned_data['grade']
            new_major = form.cleaned_data['major']

            new_student = Students(
                name=new_name,
                age = new_age,
                address = new_address,
                grade = new_grade,
                major = new_major
            )

            new_student.save()
            return render(request,'students/add_student.html', {
                'form' : StudentForm(),
                'success' : True
            })

    else:
        form = StudentForm()
        return render(request, 'students/add_student.html', {
            'form' : StudentForm()
        })
@login_required(login_url='user_login')
def edit_student(request, id):
    if request.method == 'POST':
        student = Students.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_student.html', {
                'form' : form,
                'success' : True
            })
    else:
        student = Students.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'students/edit_student.html', {
                'form' : form
            })
@login_required(login_url='user_login')
def delete_student(request,id):
    student = Students.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect(reverse('home'))