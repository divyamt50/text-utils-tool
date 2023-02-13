from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
    path('analyze', views.analyze, name = 'analyze'),
    path('about', views.about, name = 'about')
]