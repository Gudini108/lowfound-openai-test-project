from django.urls import path
from django.contrib import admin

from gpt_lowfound import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('lowfoundai/<username>/', views.lowfound_ai_view, name='lowfoundai'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('create/', views.post_create, name='post_create'),
    path('admin/', admin.site.urls),
]
