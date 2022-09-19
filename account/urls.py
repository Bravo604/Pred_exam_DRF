from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user_profile', views.ProfileViewSet, basename='user_profile')

urlpatterns = [
    path('register/sender/', views.RegisterViewSender.as_view()),
    path('register/buyer/', views.RegisterViewBuyer.as_view()),
    path('', include('rest_framework.urls')),
    path('token/', obtain_auth_token),
    path('', include(router.urls)),
]
