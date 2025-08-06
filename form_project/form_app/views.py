from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def home(request):
    return render(request, 'form_app/home.html')

def view_students(request):
    Students= Student.objects.all()
    return render(request, 'form_app/view_students.html', {'students': Students})
 
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['name']
             mark = form.cleaned_data['mark']
             Student.objects.create(name=name, mark=mark)
             return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'form_app/add_student.html', {'form': form})

def success(request):
    return render(request, 'form_app/success.html')
