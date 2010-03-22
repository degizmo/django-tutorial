from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Category(models.Model):
    Name    =    models.CharField(max_length=255)
    def __unicode__(self):
        return self.Name
    class Meta:
        verbose_name_plural = "Categories"
        
class BlogPost(models.Model):
	Title		= models.CharField(max_length=255)
	Category	= models.ForeignKey(Category)
	Slug		= models.SlugField()
	Author		= models.ForeignKey(User)
	PostText	= models.TextField()
	PublishDate	= models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
	    return self.Title
	    
admin.site.register(Category)
admin.site.register(BlogPost)

# Create your models here.
