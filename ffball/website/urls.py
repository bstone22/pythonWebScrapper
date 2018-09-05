from django.urls import path
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.response, name='respnse')
]
