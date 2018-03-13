#encoding=utf-8
# Django 项目中所有地址都需要我们自行去配置其url
"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import my_app.views as mv
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies_list/', mv.movies_list),   #一定要注意斜杠的问题
    url(r'^director_r/(?P<name>[a-zA-Z ]+)$',mv.get_director_by_rating),
    url(r'^director_g/(?P<name>[a-zA-Z ]+)$',mv.get_director_by_gross),
    url(r'^director_list/',mv.get_director_list),
    url(r'^language_list/',mv.get_language_list),
    url(r'^language/(?P<name>[a-zA-Z ]+)$',mv.get_language_detail),
    url(r'^country_list/',mv.get_country_list),
    url(r'^country/(?P<name>[a-zA-Z ]+)$',mv.get_country_detail),
    url(r'^month_list/',mv.get_month_list),
    url(r'^year_list/',mv.get_year_list),
    url(r'^year/(?P<year>[0-9a-zA-Z / .]+)$',mv.get_year),
    url(r'^production/(?P<name>[a-zA-Z / .]+)$',mv.get_production),
    url(r'^production_list/',mv.get_production_list),
    url(r'^actor_by_gross/(?P<name>[a-zA-Z /]+)$',mv.get_actor_by_gross),
    url(r'^actor_by_rating/(?P<name>[a-zA-Z /]+)$',mv.get_actor_by_rating),
    url(r'^actor_list/',mv.get_actor_list),
    url(r'^movie_by_director/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_director),
    url(r'^movie_by_director_top5/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_director_top5),
    url(r'^movie_by_production/(?P<production>[a-zA-Z / .]+)$',mv.get_movielist_by_production),
    url(r'^movie_by_production_top5/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_production_top5),
    url(r'^actor2/(?P<name>[a-zA-Z /]+)$',mv.get_actor2),
    url(r'^actor3/(?P<name>[a-zA-Z /]+)$',mv.get_actor3),
    url(r'^movie_by_actor1/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_actor1),
    url(r'^movie_by_actor2/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_actor2),
    url(r'^movie_by_actor3/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_actor3),
    url(r'^movie_by_actor_top10/(?P<name>[a-zA-Z / .]+)$',mv.get_movielist_by_actor_top10),





]

urlpatterns = format_suffix_patterns(urlpatterns)