from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Students
from .forms import StudentForm



def index(request):
    students = Students.objects.all()
    return render(request, 'index.html', {'students': students})


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Students(
                student_number=form.cleaned_data['student_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                field_to_study=form.cleaned_data['field_to_study'],
                percentage=form.cleaned_data['percentage']
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()

    return render(request, 'add.html', {
        'form': form
    })

def edit(request, id):
  if request.method == 'POST':
    student = Students.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Students.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })


def delete(request, id):
    if request.method == 'POST':
        try:
            student = Students.objects.get(pk=id)
            student.delete()
        except Students.DoesNotExist:
            # Optionally, add a message or log the error
            pass
    return HttpResponseRedirect(reverse('students:index'))