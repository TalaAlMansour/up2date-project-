from django.contrib import admin

# Register your models here.

from .models import Course, Section, Level ,News

admin.site.register(Course)

admin.site.register(Section)

admin.site.register(Level)

admin.site.register(News)