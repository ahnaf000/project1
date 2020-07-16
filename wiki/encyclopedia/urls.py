from django.urls import path

from . import views


app_name = 'encyclopedia'

urlpatterns = [

    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.querryResult, name='querryResult'),
    path("searchResult/", views.searchResult, name = 'searchResult'),
    path('test/', views.test, name='test'),
    path('newEntry/', views.newEntry, name='newEntry'),
    path('randomPage/', views.randomPage, name='randomPage'),
    path('wiki/editPage/<str:title>/', views.editPage, name='editPage'),


]












'''path("test/<str:article_name>/", views.test, name="test"),
    path("wiki/<str:title>", views.showEntry, name='showEntry'),
    path("search_wiki", views.searchEntry, name='searchEntry'),'''