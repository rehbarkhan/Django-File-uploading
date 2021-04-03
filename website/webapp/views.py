from django.shortcuts import render,redirect
from . import models
import os
# Create your views here.

def index(request):
    object_modal = models.Employee.objects.all()
    context = {
        'object_model':object_modal
    }
    return render(request,'webapp/index.html',context)

def upload_file(request):
    if request.method == "POST":
        file_name = request.POST.get('file_name')
        image = request.FILES.get('upload_file')
        object_modal = models.Employee(name=file_name,emp_image = image)
        object_modal.save()
    return redirect('/')
