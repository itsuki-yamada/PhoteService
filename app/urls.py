from django.contrib.auth import views as auth_views
from django.urls import path

from app import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>', views.users_detail, name='users_detail'),
    path('photos/post/', views.photos_post, name='photos_post'),
    path('photos/<int:pk>/', views.photos_detail, name='photos_detail'),
    path('photos/<str:category>/', views.photos_category, name='photos_category'),
    path('photos/<int:pk>/delete/', views.photos_delete, name='photos_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
