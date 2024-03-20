from django.db import models
from django.utils.text import slugify
# Create your models here.

class Course(models.Model):
    coursename = models.CharField(max_length=100 )
    def __str__(self):
     return self.coursename
    
class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    sectiontitle = models.CharField(max_length=1000)
    description = models.TextField()
    pictureSection = models.ImageField(upload_to='pictures/', null=True, blank=True,verbose_name="image")
    section_Slug=models.SlugField(null=True,blank=True)
     
    def __str__(self):
     return self.sectiontitle
    
    def save(self, *args, **kwargs):
        if not self.section_Slug:
            self.section_Slug = slugify(self.sectiontitle)
        super(Section, self).save()
    
     
       
       
    
class Level(models.Model):
    levelTitle=models.CharField(max_length=100,null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    levelDescription = models.TextField()
   # video = models.FileField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    update_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

   
       


    def __str__(self):
     return self.levelTitle
    
class News(models.Model):
    
    news_title = models.CharField(max_length=100)
    news_desc = models.TextField()
    news_date = models.DateField(null=True, blank=True)
    lessonsNum = models.IntegerField()
    newsImage = models.ImageField(upload_to='newsImage/', null=True, blank=True,verbose_name="image")





