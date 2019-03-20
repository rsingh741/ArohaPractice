from django.conf.urls import url
from . import views

urlpatterns = [
   # url('', views.post_list, name='post_list'),
    url(r'chart/', views.chart, name='chart'),
    url(r'register/', views.register, name='register')
]