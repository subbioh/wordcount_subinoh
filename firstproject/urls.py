
from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.index, name="index"),
    path('about/', wordcount.views.about, name="about"),
    path('why/', wordcount.views.why, name="why"),
    path('result/', wordcount.views.result, name="result"),
]
