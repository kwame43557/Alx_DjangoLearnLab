from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),

    # built-in class-based login view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # built-in class-based logout view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
