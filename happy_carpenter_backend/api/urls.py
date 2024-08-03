from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, api_root


urlpatterns = [
    path('', api_root, name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

