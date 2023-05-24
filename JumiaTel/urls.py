from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', views.jumiaData, name='JumiaData'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('smartphones/<int:id>/', views.smartphone_detail, name='smartphone_detail'),


]