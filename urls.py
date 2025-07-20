from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from flight_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Flight app urls
    path('', include('flight_app.urls')),

    # Authentication urls
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='flight_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='flight_list'), name='logout'),
]