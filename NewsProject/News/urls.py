

from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls

#from News.views import index, test, get_category, view_news, add_news
from News.views import HomeNews, test, NewsByCategory, ViewNews, AddNews

urlpatterns = [
    #path('', index, name = 'Home'),
    #path('category/<int:category_id>/', get_category, name='Category'),
    #path('news/<int:news_id>/', view_news, name='view_news'),
    #    path('news/add_news', add_news, name='Add_news')
    path('', HomeNews.as_view(), name='Home'),
    path('test/', test),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='View_news'),
    path('news/add_news', AddNews.as_view(), name='Add_news')
] + debug_toolbar_urls()

