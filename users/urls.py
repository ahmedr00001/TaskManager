from django.urls import path
from . import views

app_name = "users"  

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),  
    path('change-password/', views.change_password, name='change_password'),  
    
]