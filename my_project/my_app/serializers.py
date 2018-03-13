from django.contrib.auth.models import User, Group
from rest_framework import serializers
from my_app.models import movies,directors_by_gross,directors_by_rating,language,country,month_list,production,actor_by_gross,actor_by_rating,year_list,actor2,actor3

class movie_serializer(serializers.ModelSerializer):
    class Meta:
        model=movies
        fields=('id','title','year','month','production','actor1','actor2','actor3','imdbVotes','director','genre','rating','language','country','boxoffice','runtime')

        #from my_app.serializers import movie_serializer
        #serializer=movie_serializer()
        #print(repr(serializer))

class director_gross_se(serializers.ModelSerializer):
    class Meta:
        model=directors_by_gross
        fields=('rank','director','gross_box_office','number')

#Test in django shell works
# from my_app.models import movies
# from my_app.models import directors_by_gross
# from my_app.serializers import director_gross_se
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# ss=director_gross_se(directors_by_gross.objects.get(rank='1'))
# ss.data

#Convert to json format
# content=JSONRenderer().render(ss.data)
# content



class director_rating_se(serializers.ModelSerializer):
    class Meta:
        model=directors_by_rating
        fields=('rank','director','ave_rating','gross_box_office','number')


class language_se(serializers.ModelSerializer):
    class Meta:
        model=language
        fields=('id','language','rating','gross_box_office','number')

class country_se(serializers.ModelSerializer):
    class Meta:
        model=country
        fields=('id','country','rating','gross_box_office','number')

class month_list_se(serializers.ModelSerializer):
    class Meta:
        model=month_list
        fields=('id','month','gross_box_office','number','ave_gross','rating')

class year_list_se(serializers.ModelSerializer):
    class Meta:
        model=year_list
        fields=('year','gross_box_office','number','ave_gross','ave_rating')


class production_se(serializers.ModelSerializer):
    class Meta:
        model=production
        fields=('id','production','ave_gross','ave_rating','gross_box_office','number')

class actor_gross_se(serializers.ModelSerializer):
    class Meta:
        model=actor_by_gross
        fields=('rank','actor','ave_rating','gross_box_office','number')

class actor_rating_se(serializers.ModelSerializer):
    class Meta:
        model=actor_by_rating
        fields=('rank','actor','ave_rating','gross_box_office','number')

class actor2_se(serializers.ModelSerializer):
    class Meta:
        model=actor2
        fields = ('actor', 'ave_rating', 'gross_box_office','ave_gross','number')


class actor3_se(serializers.ModelSerializer):
    class Meta:
        model=actor3
        fields = ('actor', 'ave_rating', 'gross_box_office','ave_gross', 'number')



