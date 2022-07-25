from django.shortcuts import render
from .models import *


def HomeView(request):
        orders = Order.objects.all()
        customers =Customer.objects.all()
        total_customer = customers.count()
        total_orders = orders.count()
        deliverd = orders.filter(status ="Delivered").count()
        pending = orders.filter(status = "pending").count()

        context = {'orders':orders,'customers':customers,'total_orders':total_orders,'deliverd':deliverd ,'pending':pending}
        return render(request , "dashboard.html",context)
def ProductView(request):
        products = Product.objects.all()
        return render(request , "products.html",{'products' :products})
def CustomerView(request):
        return render(request , "customer.html")
# def FeedView(request):
#     return render(request , "feed.html",context)
# def ProfileView(request):
#     return render(request , "profile.html",context)

