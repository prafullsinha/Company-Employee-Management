from core.views import ProfileView,HomeView,Signup
from django.urls import path

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('signup/',Signup.as_view(),name='signup'),
    path('profile/',ProfileView.as_view(),name="profile"),
]
