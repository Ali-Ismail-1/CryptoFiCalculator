from urllib.parse import urlparse
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),    
    path('calc', views.calc, name="calculate")

]