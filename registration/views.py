from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(
        request,
        'registration/student_form.html',
        {'form': form}
    )


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'registration/student_list.html',
        {'students': students}
    )


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'registration/student_form.html',
        {
            'form': form,
            'student': student
        }
    )


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'registration/student_confirm_delete.html',
        {'student': student}
    )

def student_dashboard(request):
    students = Student.objects.all()

    total_students = students.count()

    program_counts = {}
    year_counts = {}

    for student in students:
        program_counts[student.program] = (
            program_counts.get(student.program, 0) + 1
        )

        year_counts[student.year_level] = (
            year_counts.get(student.year_level, 0) + 1
        )

    context = {
        'students': students,
        'total_students': total_students,
        'program_counts': program_counts,
        'year_counts': year_counts,
    }

    return render(
        request,
        'registration/student_dashboard.html',
        context
    )