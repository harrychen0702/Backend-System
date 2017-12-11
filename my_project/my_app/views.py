# -*- coding: utf-8 -*-
#encoding=utf-8
#执行响应的代码所在的模块，代码逻辑处理的主要地点，项目中大部分代码都在这里编写
#每一个请求都由一个函数来处理
from __future__ import unicode_literals
from rest_framework import status

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_app.models import movies
from my_app.models import directors_by_rating
from my_app.models import directors_by_gross

from my_app.serializers import movie_serializer
from my_app.serializers import director_rating_se
from my_app.serializers import director_gross_se


# Create your views here.
#每个响应对应一个函数，函数必须返回一个响应
#函数必须存在一个参数，一般约定为request
#每一个响应对应一个url


# class JSONResponse(HttpResponse):
#     """
#     用于返回JSON数据.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)




# def index(request):
#     cursor = connection.cursor()
#     cursor.execute("SELECT director FROM my_app_movies WHERE id='tt0000005' ")
#     row = cursor.fetchone()
#     return HttpResponse(row)


@api_view(['GET'])
# return first 100 movies
def movies_list(request):
    if request.method=='GET':
        movie_list=movies.objects.all()[:100]
        ss=movie_serializer(movie_list,many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_director_by_rating(request,name):
    try:
        director=directors_by_rating.objects.get(director=name)
    except directors_by_rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        ss=director_rating_se(director)
        return Response(ss.data)

@api_view(['GET'])
def get_director_by_gross(request,name):
    try:
        director=directors_by_gross.objects.get(director=name)
    except directors_by_gross.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        ss=director_gross_se(director)
        return Response(ss.data)

#测试 http://127.0.0.1:8000/director_g/Eric Notarnicola

