
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cmdb import models
from django.shortcuts import render

 #插入函数
from spider.Spider_JD import dynamic_crawler_main
from spider.Spider_level import downloadpage


def index(request):
    return render(request, 'index.html')
def university(request):
    downloadpage()
    u_list = models.message.objects.all()
    return render(request, 'rank.html', {"u_list": u_list})
def JDgoods(request):
    dynamic_crawler_main()
    jd_list = models.JDInfo.objects.all()
    return render(request, 'JD.html', {"jd_list": jd_list})