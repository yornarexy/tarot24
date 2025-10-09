from django.contrib.auth.views import LoginView, LogoutView,TemplateView
from django.urls import path, include

from .views import SignupView, upgrade_me


urlpatterns = [
    path('sign_up/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='sign_up/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm/logout/', TemplateView.as_view(template_name='sign_up/logout.html'), name='confirm_logout'),
    path('accounts/', include('allauth.urls')),
    path('upgrade/', upgrade_me, name='upgrade')

]
