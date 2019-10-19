from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', include('blog.urls')),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),

]
