from core.views import ProfileView
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('signup/',views.Signup,name='signup'),
    path('profile/',ProfileView.as_view(),name="profile"),
]
