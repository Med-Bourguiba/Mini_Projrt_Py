from django import views
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
path('JumiaTel/', include('JumiaTel.urls')),
path('admin/', admin.site.urls),
]