from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255 ,null =True)
    phone =  models.CharField(max_length=255,null =True)
    email =  models.CharField(max_length=255,null =True)
    date_created = models.DateTimeField(auto_now_add =True ,null =True)

    def __str__ (self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=255 ,null =True)

    def __str__ (self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor' ,'indoor'),
        ('outdoor' ,'outdoor'),
    )
    name = models.CharField(max_length=255 ,null =True)
    price =  models.FloatField(max_length=255,null =True)
    category =  models.CharField(max_length=255,null =True,choices = CATEGORY)
    description =  models.CharField(max_length=255,null =True, blank=True)
    date_created = models.DateTimeField(auto_now_add =True ,null =True)
    tags = models.ManyToManyField(Tag)


    def __str__ (self):
        return self.name


  

class Order(models.Model):
    STATUS = (
        ('pending' , 'pending'),
        ('out for deliver' , 'out for deliver'),
        ('Delivered' , 'Delivered'),
    )
    customer = models.ForeignKey(Customer , null =True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product , null =True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add =True ,null =True)
    status = models.CharField(max_length=255,null =True ,choices = STATUS)
    note = models.CharField(max_length=255,null =True )
    
    
   



