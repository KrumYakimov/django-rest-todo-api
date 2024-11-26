from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from todo.accounts import views

urlpatterns = [
    path("auth/register/", views.RegisterView.as_view(), name="register"),
    path("auth/login/", views.LoginView.as_view(), name="login"),
    path("auth/logout/", views.LogoutView.as_view(), name="logout"),
    path("auth/token/refresh", TokenRefreshView.as_view(), name="logout"),
]
