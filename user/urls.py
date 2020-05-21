from django.urls import path
from . import views
from .views import (
    LoginView,
    RegisterView
)

urlpatterns = [
    path('profile/', LoginView.as_view(), name='user-profile'),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('login/', views.login, name='user-login'),
]
