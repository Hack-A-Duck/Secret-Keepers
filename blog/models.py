from django.db import models
from django.db.models.fields import TextField
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    sn = models.AutoField(primary_key=True)
    title = models.CharField( max_length=200)
    author = models.CharField( max_length=20)
    Short_Description = models.TextField(max_length=400)
    content = models.TextField()
    slugs = models.CharField( max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    relation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField( max_length=40)
    email = models.CharField( max_length=200)
    phone = models.TextField(max_length=13)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)