"""techtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from articles.views import ArticlesListView, ArticleView
from author.views import AuthorListView, AuthorView
from regions.views import RegionsListView, RegionView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", csrf_exempt(ArticlesListView.as_view()), name="articles-list"),
    path("articles/<int:article_id>/", csrf_exempt(ArticleView.as_view()),
         name="article"),
    path("regions/", csrf_exempt(RegionsListView.as_view()), name="regions-list"),
    path("regions/<int:region_id>/", csrf_exempt(RegionView.as_view()), name="region"),
    path("authors/", csrf_exempt(AuthorListView.as_view()), name="authors-list"),
    path("authors/<int:author_id>/", csrf_exempt(AuthorView.as_view()),
         name="author"),
]