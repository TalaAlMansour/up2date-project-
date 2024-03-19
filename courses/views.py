
from django.shortcuts import render
from .models import Course,Section,Level,News

def courses_list(request):
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

    return render(request, 'courses.html', {'data': data})

def add_news(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        news_title = request.POST.get('news_title')
        news_desc = request.POST.get('news_desc')
        news_date = request.POST.get('news_date')
        lessons_num = request.POST.get('lessons_num')
        

        course = Course.objects.get(pk=course_id)
        news = News(course_id=course_id, news_title=news_title, news_desc=news_desc, news_date=news_date, lessonsNum=lessons_num)
        news.save()

        return render(request, 'home.html',)
    
        courses = Course.objects.all()  # Retrieve all courses to populate the form
        return render(request, 'home.html', {'courses': courses})

"""""
def leatest_courses(request):
    courses = Course.objects.prefetch_related('section_set__level_set').all()
    
    latest_levels_data = [
        {
            'course': course,
            'section': section,
            'level': section.level_set.order_by('-created_at').first()
        }
        for course in courses
        for section in course.section_set.all()
    ]

    context = {
        'latest_levels_data': latest_levels_data
    }

    return render(request, 'home.html', context)
       """


