from django.urls import path
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
    
]
