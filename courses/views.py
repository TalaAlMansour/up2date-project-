
from django.shortcuts import render
from .models import Course,Section,Level,News



def home_page(request):
    
    courses = Course.objects.prefetch_related('section_set__level_set').all()


    data = []
    for course in courses:
        course_data = {
            'course': course,
            'sections': []
        }

        for section in course.section_set.all():
            section_data = {
                'section': section,
                'levels': list(section.level_set.all())
            }

            course_data['sections'].append(section_data)

        data.append(course_data)

     
    news = News.objects.all()
    
    context = {
       
        'data': data,
        'news': news,
    }
    
    return render(request, 'home.html', context)

def section_detail(request, section_slug):
    section = Section.objects.get(section_Slug=section_slug)

    context = {
        'section': section,
        'levels': section.level_set.all()
    }

    return render(request, 'courses.html', context)