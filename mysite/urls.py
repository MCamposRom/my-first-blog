from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
#from django.urls import include, path

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url('acount/login/', views.LoginView.as_view(), name='login'),
    url('', include('blog.urls')),
    url('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    #path('admin/', admin.site.urls),
    #path('accounts/login/', views.LoginView.as_view(), name='login'),
    #path('', include('blog.urls')),
    #path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),

]
