from django.urls import path
from . views  import *

urlpatterns = [
    path('', HomeView , name ="home"),
    path('products', ProductView, name ="product"),
    path('customer', CustomerView, name ="customer"),
    # path('feed/',FeedView,name ="feeds"),
    # path('Profile/',ProfileView,name ="profile"),
]
