from django.shortcuts import render
from .models import Students

def index(request):
    students=Students.objects.all()
    return render(request,template_name='index.html',context={'students':students})
