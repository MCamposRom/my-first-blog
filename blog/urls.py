#from django.conf.urls import url
from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new', views.post_new, name='post-new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post-edit'),
    path('drafts/', views.post_draft_list, name='post-draft-list'),
    path('post/<pk>/publish/', views.post_publish, name='post-publish'),
    path('post/<pk>/remove/', views.post_remove, name='post-remove'),
]
