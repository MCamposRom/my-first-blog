from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post-list'),
    #path('', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post-detail'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
]
