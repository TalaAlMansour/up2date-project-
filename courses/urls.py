""" from .import views
from django.urls import include,path
urlpatterns = [

   path('', views.course_list, name='course_list'),
]  """
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.add_news, name='home.html'),
    path('', views.courses_list, name='courses_list'),

  #  path('/', views.leatest_courses, name='leatest_courses'),


]
