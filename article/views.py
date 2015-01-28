#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from datetime import datetime



# Create your views here.
def home(request):
    post_list = Article.objects.all() #获取全部Article对象
    return render(request,'home.html',{'post_list':post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

# def detail(request, my_args):
#     return HttpResponse("You're looking at my_args %s." % my_args)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})
