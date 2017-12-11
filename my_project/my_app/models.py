# -*- coding: utf-8 -*-
#encoding=utf-8
#数据模块，使用orm框架，类似于mvc中的models
#通常，一个model对应数据库中的一张表
#django中models以类的形式表现
#它包含了一些基本字段以及数据的一些行为
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#字段就是类里面的属性（变量）
class movies(models.Model):  #继承models.Model
    id=models.CharField(max_length=100,primary_key=True,db_column='id')
    title = models.CharField(max_length=100,  db_column='title',default='NULL')
    year=models.IntegerField(max_length=10,db_column='year',default=0)
    month=models.CharField(max_length=10,db_column='month',default='NULL')
    production=models.CharField(max_length=100,db_column='production',default='NULL')
    actor1=models.CharField(max_length=30,db_column='actor1',default='NULL')
    actor2 = models.CharField(max_length=30, db_column='actor2',default='NULL')
    actor3 = models.CharField(max_length=30, db_column='actor3',default='NULL')
    imdbVotes=models.IntegerField(max_length=100,db_column='imdbVotes',default=0)
    director=models.CharField(max_length=100,db_column='director',default='NULL')
    genre=models.CharField(max_length=100,db_column='genre',default='NULL')
    rating=models.FloatField(db_column='rating',default=0)
    language=models.CharField(max_length=100,db_column='language',default='NULL')
    country=models.CharField(max_length=50,db_column='country',default='NULL')
    boxoffice=models.FloatField(db_column='boxoffice',default=0)
    runtime=models.IntegerField(max_length=10,db_column='runtime',default=0)


class directors_by_gross(models.Model):
    rank=models.IntegerField(primary_key=True,db_column='rank')
    director=models.CharField(max_length=100,db_column='director',default='NULL')
    gross_box_office=models.FloatField(db_column='gross_box_office',default=0)
    number = models.IntegerField(db_column='number',default=0)

class directors_by_rating(models.Model):
    rank = models.IntegerField(primary_key=True, db_column='rank')
    director = models.CharField(max_length=100, db_column='director', default='NULL')
    ave_rating=models.FloatField(db_column='rating',default=0)
    number = models.IntegerField(db_column='number', default=0)


