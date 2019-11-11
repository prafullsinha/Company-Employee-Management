from core.views import ProfileView, HomeView, ManagerView, CompanyView, Signup2, NormalView
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
                  path('', HomeView.as_view(), name='home'),
                  path('normal/', NormalView.as_view(), name='normal'),
                  path('company/', CompanyView.as_view(), name='company'),
                  path('signup2/', Signup2.as_view(), name='signup2'),
                  path('profile/', ProfileView.as_view(), name="profile"),
                  path('member/', ManagerView.as_view(), name="manager"),
                  path('member/<str:email>/', views.ManagerMemberView, name="member"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
