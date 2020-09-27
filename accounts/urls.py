from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import UserView, signup,ProfileView


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/home/', UserView.as_view(), name='home'),
    path('signup/', signup, name='signup'),
    path('profile/',ProfileView.as_view(),name='profile')
]