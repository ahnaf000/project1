from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("test/<str:article_name>/", views.test, name="test"),
    path("wiki/<str:title>", views.showEntry, name='showEntry'),
    path("search_wiki", views.searchEntry, name='searchEntry'),

]
