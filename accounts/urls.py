from django.urls import path
from django.contrib.auth import views as auth_views
from . views  import *

urlpatterns = [
    path('', HomeView , name ="home"),
    path('products', ProductView, name ="product"),
    path('register', RegisterView, name ="register"),
    path('login', LoginView, name ="login"),
     path('logout', LogOutView, name ="logout"),
    path('create/<str:pk>', CreateView, name ="create"),
    path('customer/<str:pk>', CustomerView, name ="customer"),
    path('update/<str:pk>', UpdateView, name ="update"),
    path('delete/<str:pk>', DeleteView, name ="delete"),
    path('user',UserPage, name="user"),
    path('account',AccountView , name='account'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
    
]
