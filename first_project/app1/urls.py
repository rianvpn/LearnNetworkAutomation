from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('page1', views.page1),
    path('page2', views.page2)
]
