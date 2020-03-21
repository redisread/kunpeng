# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
# 表单
def search_form(request):
    context = None
    return render(None, 'search_form.html', context)
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)