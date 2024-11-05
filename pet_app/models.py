from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name="Is admin")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")
    is_customer = models.BooleanField(default=False, verbose_name="Is Customer")
    is_boy = models.BooleanField(default=False, verbose_name="Is Delivery Boy")
    name = models.CharField(max_length=100,null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=20,null=True, blank=True)
    role = models.CharField(max_length=20,null=True, blank=True)
    photo = models.ImageField(upload_to='profile/',null=True, blank=True)

    @property
    def imageURL_2(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return  url

class Category(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

class Category_pet(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

class Pet(models.Model):
    name = models.CharField(max_length=100,null=False)
    category = models.ForeignKey(Category_pet,on_delete=models.CASCADE,null=True,blank=True)
    pic = models.ImageField(upload_to='pet/',null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    description =models.CharField(max_length=300,null=False)
    breed=models.CharField(max_length=200,null=False)
    color=models.CharField(max_length=100,null=False)
    stock_level=models.IntegerField(null=False)
    age=models.CharField(max_length=100,null=False)
    vaccination = models.CharField(max_length=300,null=True)
    

    
    @property
    def imageURL(self):
        try:
            url = self.pic.url
        except:
            url = ''
        return  url
    
class Products(models.Model):
    name =models.CharField(max_length=100,null=False)    
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='product/',null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True) 
    description = models.CharField(max_length=300,null=False)
    stock_level =models.IntegerField(null=False)

    @property
    def imageURL_1(self):
        try:
            url = self.pic.url
        except:
            url = ''
        return  url

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        if self.product:
            return self.product.price * self.quantity
        elif self.pet:
            return self.pet.price * self.quantity
        return 0
    
class Checkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    holder_name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Checkout for {self.user.name} on {self.created_at}"
    

class CheckoutItem(models.Model):
    boys = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boys', verbose_name="boys",null=True)
    checkout = models.ForeignKey(Checkout, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, null=True, blank=True)

class Pet_book(models.Model):
    cust = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', verbose_name="customer",null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.PositiveIntegerField(default=1,null=True, blank=True)
    holder_name = models.CharField(max_length=255,null=True, blank=True)
    ac_number = models.CharField(max_length=255,null=True, blank=True)
    advance_amount = models.IntegerField(null=True, blank=True)
    balance_amount = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
