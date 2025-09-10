from django.shortcuts import render, get_object_or_404
from .models import Student

def welcome(request):
    return render(request, 'students/welcome.html')

def bye(request):
    return render(request, 'students/bye.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_details(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_details.html', {'student': student})
