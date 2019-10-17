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
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add-comment-to-post'),
    path('post/<pk>/comment/', views.add_comment_to_post, name='add-comment-to-post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment-approve'),
    path('comment/<pk>/approve/', views.comment_approve, name='comment-approve'),
    #url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment-remove'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment-remove'),

]
