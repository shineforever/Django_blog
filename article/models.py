#coding:utf-8

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)  #blog题目
    category = models.CharField(max_length = 50,blank = True) #blog 标签
    date_time = models.DateTimeField(auto_now_add = True) # blog日期
    content = models.TextField(blank = True,null = True)  #blog文章内容

    def __unicode__(self):
        return self.title

    class Meta:
        """
        按照文章时间的，降序排序
        """
        ordering = ['-date_time']