from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min, StdDev
from .forms import EducationForm
from .models import EducationProgram

def program_form(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_list')
    else:
        form = EducationForm()
    return render(request, 'education/form.html', {'form': form})

def data_list(request):
    programs = EducationProgram.objects.all()
    
    # Фильтрация
    program_filter = request.GET.get('program')
    if program_filter:
        programs = programs.filter(program_name=program_filter)
    
    # Сортировка
    sort = request.GET.get('sort')
    if sort:
        programs = programs.order_by(sort)
    
    # Уникальные программы для фильтра
    unique_programs = EducationProgram.objects.values_list(
        'program_name', flat=True
    ).distinct()
    
    return render(request, 'education/data_list.html', {
        'programs': programs,
        'unique_programs': unique_programs,
    })

def statistics(request):
    stats = EducationProgram.objects.aggregate(
        avg_score=Avg('score'),
        max_score=Max('score'),
        min_score=Min('score'),
        std_dev=StdDev('score')
    )
    return render(request, 'education/stats.html', {'stats': stats})