from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.home, name='home'),  
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    url(r'^login/$', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
  
]
