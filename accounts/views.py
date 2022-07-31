from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate , login,logout
from .forms import CreateOrderForm ,CreateUserForm,CustomerForm
from django.contrib import messages
from django.forms import inlineformset_factory
from .filters import OrderFilter
from .decorators import unauthenticated_user,allowed_users,admin_only

from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
@admin_only
# @allowed_users(allowed_roles=['admin'])
def HomeView(request):
        orders = Order.objects.all()
        customers =Customer.objects.all()
        total_customer = customers.count()
        total_orders = orders.count()
        deliverd = orders.filter(status ="Delivered").count()
        pending = orders.filter(status = "pending").count()

        context = {'orders':orders,'customers':customers,'total_orders':total_orders,'deliverd':deliverd ,'pending':pending}
        return render(request , "dashboard.html",context)

@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def UserPage(request):
        orders = request.user.customer.order_set.all()
        total_orders = orders.count()
        deliverd = orders.filter(status ="Delivered").count()
        pending = orders.filter(status = "pending").count()
     
        context ={'orders': orders,'total_orders':total_orders,'deliverd':deliverd,'pending':pending}
        return render(request,'user.html',context)
def ProductView(request):
        products = Product.objects.all()
        return render(request , "products.html",{'products' :products})
def CustomerView(request , pk):
       customer = Customer.objects.get(id=pk)
       orders = customer.order_set.all()
       myFilter = OrderFilter(request.GET,queryset=orders)
       orders = myFilter.qs
       total_orders = orders.count()
       context = {'customer':customer,'orders':orders ,'total_orders':total_orders ,'myFilter':myFilter}
       return render(request , "customer.html",context)
def CreateView(request,pk):
        # print("pronting now",request.POST) checking if the data is sented from the form
       form = CreateOrderForm()
       if request.method == "POST":
          form = CreateOrderForm(request.POST)
          if form.is_valid():
                form.save()
                return redirect("/")
       context ={'form':form}
       return render(request ,"order_form.html",context)

def UpdateView(request,pk):
    #  to update aform it must be already filled for so we get all instances of the order then give it to the form
        order = Order.objects.get(id=pk)
        form = CreateOrderForm(instance = order)
        if request.method == "POST":
            form = CreateOrderForm(request.POST,instance=order)
            if form.is_valid():
                form.save()
                return redirect("/")
       
        context = {'form':form}
        return render(request ,"order_form.html",context)


def DeleteView(request,pk):
        order = Order.objects.get(id=pk)
        if request.method =="POST":
            order.delete()
            return redirect("/")
        context = {'item':order}
        return render(request ,"delete.html",context)     

@unauthenticated_user
def RegisterView(request):
                form = CreateUserForm()
                if request.method == 'POST':
                        form = CreateUserForm(request.POST)
                        if form.is_valid():
                                user = form.save()
                                username = form.cleaned_data.get('username')
                                messages.success(request, 'account was sucessfully created for ' + username)
                        
                        
                                return redirect("login")
                context ={'form':form}
                return render(request , 'register.html', context)
     
@unauthenticated_user
def LoginView(request):
                if request.method =="POST":
                        username = request.POST.get('username')
                        password= request.POST.get('password')
                        user = authenticate(request,username =username,password=password)
                        # if user.is_authenticated():
                
                        if user is not None:
                                login(request ,user)
                                return redirect("home")
                        else:
                                messages.info(request, 'username or password incorrect')

                context ={}
                return render(request , 'login.html', context)
def LogOutView(request):
        logout(request)
        return redirect("login")
@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def AccountView(request):
        customer= request.user.customer
        form =CustomerForm(instance=customer)
        if request.method=="POST":
           form =CustomerForm(request.POST,request.FILES,instance=customer)
           if form.is_valid():
                form.save()

        context ={'form':form}
        return render(request , 'account_setting.html',context)


       