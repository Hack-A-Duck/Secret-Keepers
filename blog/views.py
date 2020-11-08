from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact
import math
# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-time')[:3]
    context = {"blogs":blogs}
    return render(request,'home.html',context)

def blog(request):
    no_of_post = 4
    page = request.GET.get("page")
    if (page is None):
        page = 1
    else:
        page = int(page)
    allblogs = Blog.objects.all().order_by('-time')
    total = len(allblogs)
    blogs = allblogs[((page-1)*no_of_post):(page*no_of_post)]

    if page>1:
        prev = page-1
    else:
        prev = None
    num = math.ceil(total/no_of_post)
    if page<num:
        nxt = page + 1
    else:
        nxt = None
    context = {"blogs":blogs,"prev":prev,"nxt":nxt}
    return render(request,'bloghome.html',context)


def contact(request):
    if request.method =='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        instance = Contact(name=name, email = email, phone =phone, message = message)
        instance.save()

    
    return render(request,'contact.html')


def blogpost(request, slug):
    blog = Blog.objects.filter(slugs=slug).first()
    context = {"blogs":blog}
    return render(request,'blogpost.html',context)



def search(request):
    queries = request.GET['query']
    allposts = Blog.objects.filter(title__icontains=queries)
    params = {"blogs":allposts,"que":queries}




    return render(request,'search.html',params)




def about(request):
    return render(request,'about.html',)