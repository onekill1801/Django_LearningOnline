from django.urls import path
from . import views
from .views import (
    MyCourserView,
    AllCourserView
)

urlpatterns = [
    path('', MyCourserView.as_view(), name='courses-home'),
    path('mycourses/', MyCourserView.as_view(), name='courses-my'),
    path('allcourses/', AllCourserView.as_view(), name='courses-all'),
]
