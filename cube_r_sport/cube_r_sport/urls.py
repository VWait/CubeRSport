from django.contrib import admin
from django.urls import path, include

# from  import views

from cube_r_sport.view import Hello

urlpatterns = [
    path('', Hello.as_view()),
    path('admin/', admin.site.urls)
]
