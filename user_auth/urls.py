from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LogInUserAPIView, RegisterUserAPIView

urlpatterns = [
    path('login/', LogInUserAPIView.as_view()),
    path('register/', RegisterUserAPIView.as_view()),
]
