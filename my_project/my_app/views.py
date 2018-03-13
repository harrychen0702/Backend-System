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
from my_app.models import language,country,month_list
from my_app.models import production,actor_by_gross,actor_by_rating,year_list,actor3,actor2

from my_app.serializers import movie_serializer
from my_app.serializers import director_rating_se
from my_app.serializers import director_gross_se
from my_app.serializers import language_se,country_se,month_list_se,production_se,actor_gross_se,actor_rating_se,year_list_se,actor2_se,actor3_se


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

@api_view(['GET'])
def get_director_list(request):
    if (request.method == 'GET'):
        a1 = directors_by_rating.objects.all()
        a2 = director_rating_se(a1, many=True)
        return Response(a2.data)


#测试 http://127.0.0.1:8000/director_g/Eric Notarnicola

@api_view(['GET'])
def get_language_list(request):
    if(request.method=='GET'):
        language_list=language.objects.all()[:50]
        ss=language_se(language_list,many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_language_detail(request,name):
    try:
        language1=language.objects.get(language=name)
    except language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method=='GET'):
        ss=language_se(language1)
        return Response(ss.data)

@api_view(['GET'])
def get_country_list(request):
    if (request.method == 'GET'):
        country_list = country.objects.all()
        ss = country_se(country_list, many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_country_detail(request,name):
    try:
        country1=country.objects.get(country=name)
    except country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method=='GET'):
        ss=country_se(country1)
        return Response(ss.data)

@api_view(['GET'])
def get_month_list(request):
    if(request.method== 'GET'):
        month_list1=month_list.objects.all()
        ss=month_list_se(month_list1,many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_year_list(request):
    if(request.method== 'GET'):
        year_list1=year_list.objects.all()
        ss=year_list_se(year_list1,many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_year(request,year):
    if(request.method== 'GET'):
        year_detail=year_list.objects.get(year=year)
        ss=year_list_se(year_detail)
        return Response(ss.data)

@api_view(['GET'])
def get_production(request,name):
    try:
        p1=production.objects.get(production=name)
    except production.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        p2=production_se(p1)
        return Response(p2.data)

@api_view(['GET'])
def get_production_list(request):
    if(request.method== 'GET'):
        p_list1=production.objects.all()
        ss=production_se(p_list1,many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_movielist_by_production_top5(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(production=name).order_by('-rating')[:5] ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)


@api_view(['GET'])
def get_actor_by_gross(request,name):
    try:
        a1=actor_by_gross.objects.get(actor=name)
    except actor_by_gross.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        a2=actor_gross_se(a1)
        return Response(a2.data)

@api_view(['GET'])
def get_actor_by_rating(request,name):
    try:
        a1 = actor_by_rating.objects.get(actor=name)
    except actor_by_rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        a2 = actor_rating_se(a1)
        return Response(a2.data)

@api_view(['GET'])
def get_actor_list(request):
    if (request.method == 'GET'):
        a1 = actor_by_rating.objects.all()
        a2 = actor_rating_se(a1,many=True)
        return Response(a2.data)


@api_view(['GET'])
def get_movielist_by_director(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(director=name).order_by('-year').reverse() ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)


@api_view(['GET'])
def get_movielist_by_director_top5(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(director=name).order_by('-rating')[:5] ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_movielist_by_production(request,production):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(production=production).order_by('-year').reverse() ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_actor2(request,name):
    try:
        a1 = actor2.objects.get(actor=name)
    except actor2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        a2 = actor2_se(a1)
        return Response(a2.data)

@api_view(['GET'])
def get_actor3(request,name):
    try:
        a1 = actor3.objects.get(actor=name)
    except actor3.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        a2 = actor3_se(a1)
        return Response(a2.data)


@api_view(['GET'])
def get_movielist_by_actor1(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(actor1=name).order_by('-year').reverse() ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_movielist_by_actor2(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(actor2=name).order_by('-year').reverse() ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_movielist_by_actor3(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(actor3=name).order_by('-year').reverse() ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)

@api_view(['GET'])
def get_movielist_by_actor_top10(request,name):
    if(request.method=='GET'):
        movie_list = movies.objects.filter(actor1=name).order_by('-rating')[:7] ##order by year in ascending order
        ss = movie_serializer(movie_list, many=True)
        return Response(ss.data)