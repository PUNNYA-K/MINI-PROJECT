from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    return render(request,'index.html')

############admin panel ##############
#####################################

##############Admin register ##################

def admin_register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("password")
        passw2= request.POST.get("password1")
        
        if passw1 ==passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'admin/register.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                  
                    is_admin=True,
                )
                user.save()
                # Add a success message
                messages.success(request, 'Registration successful.')
                return redirect('admin_login')
        else:
            messages.error(request, 'password not matching.')
            return redirect('admin_register')
        
    else:
        return render(request, "admin/register.html")
    

#############login #########################
def admin_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_admin:
            login(request, user)
            return redirect('adm_home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "admin/login.html")

########admin home #######
def adm_home(request):
    boy=User.objects.filter(is_boy=True)
    staff=User.objects.filter(is_staff=True)
    context={
        'boy':boy,
        'staff':staff
    }
    return render(request,'admin/index.html',context)

##############staff register ##################

def staff_register(request):
    staff=User.objects.filter(is_staff=True)
    
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("Password")
        passw2= request.POST.get("Password1")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        Role = request.POST.get("Role")
        
        if passw1 ==passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'admin/add_staff.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    name=name,
                    mobile=phone,
                    email=email,
                    role=Role,
                    is_staff=True,
                )
                user.save()
                # Add a success message
                messages.success(request, 'Registration successful.')
                return redirect('staff_register')
        else:
            messages.error(request, 'password not matching.')
            return redirect('staff_register')
    
    else:
        context={
        'staff':staff
    }
        return render(request, "admin/add_staff.html",context)

##### delete shop
def delete_staff(request,pk):
    staff=User.objects.get(pk=pk)
    staff.delete()
    messages.error(request, 'Delete Successfully Completed.')
    return redirect('staff_register')  

##############staff register ##################

def boy_register(request):
    boy=User.objects.filter(is_boy=True)
    
    if request.method == "POST":
        uname = request.POST.get("username")
        passw1 = request.POST.get("Password")
        passw2= request.POST.get("Password1")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        Role = request.POST.get("Role")
        
        if passw1 ==passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'admin/add_boy.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    name=name,
                    mobile=phone,
                    email=email,
                    role=Role,
                    is_boy=True,
                )
                user.save()
                # Add a success message
                messages.success(request, 'Registration successful.')
                return redirect('boy_register')
        else:
            messages.error(request, 'password not matching.')
            return redirect('boy_register')
    
    else:
        context={
        'boy':boy
    }
        return render(request, "admin/add_boy.html",context)
    

##### delete shop
def delete_boy(request,pk):
    boys=User.objects.get(pk=pk)
    boys.delete()
    messages.error(request, 'Delete Successfully Completed.')
    return redirect('boy_register')
  
def add_category(request): 
    cate=Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name').strip()  # Trim whitespace
        # Check if category with the same name already exists
        if Category.objects.filter(name__iexact=name).exists():
            messages.error(request, 'Category with the same name already exists.')
        else:
            # Create and save the category if it does not exist
            category = Category.objects.create(name=name)
            category.save()
            messages.success(request, 'Category added successfully.')
            return redirect('add_category')
    context={
        'cate':cate
    }
  

    return render(request, "admin/add_category.html",context)


def add_pet_category(request): 
    cate=Category_pet.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name').strip()  # Trim whitespace
        # Check if category with the same name already exists
        if Category_pet.objects.filter(name__iexact=name).exists():
            messages.error(request, 'Category with the same name already exists.')
        else:
            # Create and save the category if it does not exist
            category = Category_pet.objects.create(name=name)
            category.save()
            messages.success(request, 'pet Category added successfully.')
            return redirect('add_pet_category')
    context={
        'cate':cate
    }
  
    return render(request, "admin/pet_category.html",context)

##### delete shop
def delete_pet_category(request,pk):
    boys=Category_pet.objects.get(pk=pk)
    boys.delete()
    messages.error(request, 'Delete Successfully Completed.')
    return redirect('add_pet_category')

##### delete shop
def delete_category(request,pk):
    boys=Category.objects.get(pk=pk)
    boys.delete()
    messages.error(request, 'Delete Successfully Completed.')
    return redirect('add_category')

def Logout(request):  
    logout(request)
    return redirect('cus_home')
  
#######update staff 


def update_staff(request,pk):
    update=User.objects.get(pk=pk)
    if request.method == 'POST':
        update.username=request.POST.get('username')
        update.name=request.POST.get('name')
        update.mobile=request.POST.get('phone') 
        update.email=request.POST.get('email') 
        update.role=request.POST.get('Role') 
        update.save()
        messages.success(request,"Update successfully")
        return redirect('staff_register')
    context={
        'update':update
    }
    return render(request,'admin/edit_staff.html',context)

#######update boys 


def update_boy(request,pk):
    update=User.objects.get(pk=pk)
    if request.method == 'POST':
        update.username=request.POST.get('username')
        update.name=request.POST.get('name')
        update.mobile=request.POST.get('phone') 
        update.email=request.POST.get('email') 
        update.role=request.POST.get('Role') 
        update.save()
        messages.success(request,"Update successfully")
        return redirect('boy_register')
    context={
        'update':update
    }
    return render(request,'admin/edit_boy.html',context)

def all_order_history_view(request):
    # Retrieve all checkout items, ordered by the `created_at` field in the related Checkout model
    orders = CheckoutItem.objects.all().order_by('-checkout__created_at')
    return render(request, 'admin/order_history.html', {'orders': orders})



def assign_work(request, pk):
    # Retrieve the CheckoutItem using the provided primary key (pk)
    checkout_item = get_object_or_404(CheckoutItem, checkout_id=pk)
    boys = User.objects.filter(is_boy=True)

    if request.method == 'POST':
        # Get the selected boy and status from the form
        selected_boy_id = request.POST.get('boy')
        selected_status = request.POST.get('status')

        if selected_boy_id:
            try:
                # Retrieve the selected boy user object
                selected_boy = User.objects.get(id=selected_boy_id)
                checkout_item.boys = selected_boy  # Assign the selected boy
            except User.DoesNotExist:
                messages.error(request, "Selected boy does not exist.")

        # Update the status if it's provided
        if selected_status:
            checkout_item.status = selected_status

        # Save the updated checkout item
        checkout_item.save()

        # Show a success message and redirect if needed
        messages.success(request, "Work assigned successfully.")
        return redirect('all_order_history_view')  # Replace with your desired redirect view name

    context = {
        'checkout_item': checkout_item,
        'boys': boys
    }
    return render(request, 'admin/assign_work.html', context)

def all_pet_history_view(request):
    # Retrieve all checkout items, ordered by the `created_at` field in descending order
    orders = Pet_book.objects.all().order_by('-created_at')
    return render(request, 'admin/pet_history.html', {'orders': orders})



def product_payment(request):
    # Retrieve all checkout items, ordered by the `created_at` field in the related Checkout model
    orders = CheckoutItem.objects.all().order_by('-checkout__created_at')
    return render(request, 'admin/product_payment.html', {'orders': orders})

def pet_payment(request):
    # Retrieve all checkout items, ordered by the `created_at` field in the related Checkout model
    orders = Pet_book.objects.all().order_by('created_at')
    return render(request, 'admin/pet_payment.html', {'orders': orders})

from datetime import datetime
def sales_report(request):
    # Get the date range from the GET request
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if from_date and to_date:
        # Convert string date inputs to datetime objects
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        to_date = datetime.strptime(to_date, '%Y-%m-%d')

        # Total sales from Checkout model
        total_sales = Checkout.objects.filter(created_at__range=[from_date, to_date]).aggregate(total=Sum('total_amount'))['total'] or 0

        # Total orders from Checkout model
        total_orders = Checkout.objects.filter(created_at__range=[from_date, to_date]).count()

        # Total pet bookings from Pet_book model
        total_bookings = Pet_book.objects.filter(created_at__range=[from_date, to_date]).count()

        # Total quantity and sales by products and pets from CheckoutItem model
        product_sales = CheckoutItem.objects.filter(checkout__created_at__range=[from_date, to_date]).aggregate(total_sales=Sum('total_price'), total_quantity=Sum('quantity'))

    else:
        # If no date range is provided, set default values
        total_sales = 0
        total_orders = 0
        total_bookings = 0
        product_sales = {'total_sales': 0, 'total_quantity': 0}

    context = {
        'total_sales': total_sales,
        'total_orders': total_orders,
        'total_bookings': total_bookings,
        'product_sales': product_sales,
        'from_date': from_date,
        'to_date': to_date,
    }

    return render(request, 'admin/report.html', context)

##############staff  register ##################
###################################################

########admin home #######
def staff_home(request):
    return render(request,'staff/index.html')
# #############login #########################
# def staff_login(request):  
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         passw = request.POST.get('password')

#         user = User.objects.filter(username=uname).first()
        
#         if user is not None and user.check_password(passw) and user.is_staff :
#             login(request, user)
#             return redirect('staff_home')
#         else:
#             messages.error(request, 'Invalid login credentials.')
#     return render(request, "staff/login.html")

############# add pet details #################

def add_pet(request):
    pets=Pet.objects.all()
    category=Category_pet.objects.all()
    if request.method == "POST":
        

        pet=Pet()
        
        pet.name=request.POST.get('name')
        

         # Get the category name from the form data
        category_name = request.POST.get('category')
         # Assuming you have a 'Category' model and a field 'name'
        # Retrieve the Category instance based on the name
        category_instance = Category_pet.objects.get(name=category_name)

        pet.category = category_instance

        pet.price=request.POST.get('price')
        pet.description=request.POST.get('description')
        pet.breed=request.POST.get('breed')
        pet.color=request.POST.get('color')
        pet.stock_level=request.POST.get('StockLevel')
        pet.age=request.POST.get('Age')
        pet.vaccination=request.POST.get('vaccination')

        if len(request.FILES)!= 0:
            pet.pic=request.FILES["img"]
        
        pet.save()
        messages.success(request,"Pet Created successfully")
        return redirect('add_pet')   
    context={
        'category':category,
        'pets':pets
    }
    return render(request,'staff/add_pet.html',context)
import os
def update_pet(request,pk):
    category=Category_pet.objects.all()
    update=Pet.objects.get(pk=pk)
    if request.method == 'POST':
        update.name=request.POST.get('name')
        

         # Get the category name from the form data
        category_name = request.POST.get('category')
         # Assuming you have a 'Category' model and a field 'name'
        # Retrieve the Category instance based on the name
        category_instance = Category_pet.objects.get(name=category_name)

        update.category = category_instance

        update.price=request.POST.get('price')
        update.description=request.POST.get('description')
        update.breed=request.POST.get('breed')
        update.color=request.POST.get('color')
        update.stock_level=request.POST.get('StockLevel')
        update.age=request.POST.get('Age')
        update.vaccination=request.POST.get('vaccination')
        if 'img' in request.FILES:
            # Remove the old image file if it exists
            if update.pic:
                os.remove(update.pic.path)
            # Update the image field with the new file
            update.pic = request.FILES['img']
        
        update.save()
        messages.success(request,"Update successfully")
        return redirect('add_pet')
    context={
        'update':update,
        'category':category,
    }
    return render(request,'staff/edit_pet.html',context)

##### delete pet
def delete_pet(request,pk):
    pet=Pet.objects.get(pk=pk)
    pet.delete()
    messages.error(request, 'Delete Successfully Completed.')
    return redirect('add_pet')

############# add product details #################

def add_product(request):
    product=Products.objects.all()
    category=Category.objects.all()
    if request.method == "POST":
        produc=Products()
        
        produc.name=request.POST.get('name')
        

         # Get the category name from the form data
        category_name = request.POST.get('category')
         # Assuming you have a 'Category' model and a field 'name'
        # Retrieve the Category instance based on the name
        category_instance = Category.objects.get(name=category_name)

        produc.category = category_instance

        produc.price=request.POST.get('price')
        produc.description=request.POST.get('description')
       
        produc.stock_level=request.POST.get('StockLevel')
        

        if len(request.FILES)!= 0:
            produc.pic=request.FILES["img"]
        
        produc.save()
        messages.success(request,"Product Created successfully")
        return redirect('add_product')   
    context={
        'category':category,
        'product':product
    }
    return render(request,'staff/add_product.html',context)


def update_product(request,pk):
    category=Category.objects.all()
    update=Products.objects.get(pk=pk)
    if request.method == 'POST':
        update.name=request.POST.get('name')
        

         # Get the category name from the form data
        category_name = request.POST.get('category')
         # Assuming you have a 'Category' model and a field 'name'
        # Retrieve the Category instance based on the name
        category_instance = Category.objects.get(name=category_name)

        update.category = category_instance

        update.price=request.POST.get('price')
        update.description=request.POST.get('description')
      
        update.stock_level=request.POST.get('StockLevel')
  
       
        if 'img' in request.FILES:
            # Remove the old image file if it exists
            if update.pic:
                os.remove(update.pic.path)
            # Update the image field with the new file
            update.pic = request.FILES['img']
        
        update.save()
        messages.success(request,"Update successfully")
        return redirect('add_product')
    context={
        'update':update,
        'category':category,
    }
    return render(request,'staff/edit_product.html',context)

##### delete pet
def delete_product(request,pk):
    pet=Products.objects.get(pk=pk)
    pet.delete()
    messages.error(request, 'Delete Successfully Completed.')
    return redirect('add_product')
##############Customer  register ##################
###################################################
def cus_register(request):

    
    if request.method == "POST":
        uname = request.POST.get("username")
        name = request.POST.get("name")
        passw1 = request.POST.get("password")
        passw2= request.POST.get("password1")
       
        phone = request.POST.get("Phone")
        email = request.POST.get("Email")
        Role = request.POST.get("Role")
        address = request.POST.get("address")
        photo=request.FILES.get('img')
        
        if passw1 ==passw2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'user/register.html')
            else:
                user = User.objects.create_user(
                    username=uname,
                    password=passw1,
                    name=name,
                  
                    mobile=phone,
                    email=email,
                    Address=address,
                    role=Role,
                    photo=photo,
                    is_customer=True,
                )
                user.save()
                # Add a success message
                messages.success(request, 'Registration successful.')
                return redirect('cus_login')
        else:
            messages.error(request, 'password not matching.')
            return redirect('cus_register')
    
    else:
        
    
        return render(request, "user/register.html")
    
def cus_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_customer:
            login(request, user)
            return redirect('cus_home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "user/login.html")

def cus_home(request):
    category=Category.objects.all()
    category_1=Category_pet.objects.all()
    context={
        
        'category':category,
        'category_1':category_1,
    }
    return render(request,'user/index.html',context)

def pet_details(request,pk):
    category = Category_pet.objects.get(pk=pk)
    pets = Pet.objects.filter(category=category)

    context = {
        'category': category,
        'pets': pets,
       
        
    }
    return render(request,'user/pets_details.html',context)

def product_detail(request,pk):
    category = Category.objects.get(pk=pk)

    products = Products.objects.filter(category=category)
    context = {
        'category': category,
        
        'products': products,
        
    }
    return render(request,'user/product_details.html',context)

def product_details(request,pk):

    product = Products.objects.get(pk=pk)

    context = {
   
        'product': product
    }
    return render(request,'user/product_full.html',context)

def pet_full_details(request,pk):
    
    pet = Pet.objects.get(pk=pk)
    context = {
        'pet': pet,
      
    }
    return render(request,'user/pets_full.html',context)

# def add_to_cart(request):
  
#     return render(request,'user/add_to_cart.html')
@login_required(login_url='cus_login')
def add_to_cart(request, product_id=None, pet_id=None):
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if product_id:
        product = get_object_or_404(Products, id=product_id)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    elif pet_id:
        pet = get_object_or_404(Pet, id=pet_id)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, pet=pet)
    else:
        return redirect('cus_home')

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')

@login_required(login_url='cus_login')
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'user/add_to_cart.html', {'cart': cart})
@login_required(login_url='cus_login')
def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart_detail')  # Redirect back to cart page
@login_required(login_url='cus_login')
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    return redirect('cart_detail')
@login_required(login_url='cus_login')
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()  # Remove the item from the cart
    return redirect('cart_detail')




from django.utils import timezone
from decimal import Decimal


@login_required(login_url='cus_login')
def checkout_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()

    if not cart or not cart.items.exists():
        messages.error(request, "No items in cart.")
        return redirect('cart_detail')

    if request.method == "POST":
        # Capture form data
        account_number = request.POST.get("card-number")
        holder_name = request.POST.get("name")
        expiry = request.POST.get("expiry")

        # Parse and validate the expiry date
        try:
            expiry_date = timezone.datetime.strptime(expiry, "%m/%y").date()
        except ValueError:
            messages.error(request, "Invalid expiration date format. Use MM/YY.")
            return render(request, 'user/card.html', {"cart": cart})

        # Calculate total amount
        total_amount = Decimal(cart.total_price)

        # Save the checkout instance
        checkout = Checkout.objects.create(
            user=user,
            cart=cart,
            account_number=account_number,
            holder_name=holder_name,
            expiry_date=expiry_date,
            total_amount=total_amount
        )
        checkout.save()
        # Save each item in the cart as a CheckoutItem
        for item in cart.items.all():
            product_name = item.product.name if item.product else item.pet.name
            item_total_price = item.total_price
            quantity = item.quantity

            # Save the CheckoutItem
            CheckoutItem.objects.create(
                checkout=checkout,
                product_name=product_name,
                quantity=quantity,
                total_price=item_total_price
            )

        # After checkout is saved, update stock levels and clear items in the cart
        for item in cart.items.all():
            if item.product:
                item.product.stock_level -= item.quantity
                if item.product.stock_level <= 0:
                    item.product.stock_level = 0  # Ensure stock level doesn't go below zero
                    item.delete()  # Remove product from cart if out of stock
                item.product.save()
            elif item.pet:
                item.pet.stock_level -= item.quantity
                if item.pet.stock_level <= 0:
                    item.pet.stock_level = 0  # Ensure stock level doesn't go below zero
                    item.delete()  # Remove pet from cart if out of stock
                item.pet.save()

        # Clear the cart after processing items
        cart.items.all().delete()

        
        return redirect('checkout-success')

    # Render the checkout page for GET requests
    return render(request, 'user/card.html', {"cart": cart})

@login_required(login_url='cus_login')
def checkout_success(request):
    return render(request, 'user/checkout_success.html')

@login_required(login_url='cus_login')
def order_history_view(request):
    user = request.user
    # Get all checkout items for the current user, ordered by the `created_at` field in the related Checkout model
    orders = CheckoutItem.objects.filter(checkout__user=user).order_by('-checkout__created_at')
    return render(request, 'user/view_history.html', {'orders': orders})

##############staff  register ##################
###################################################

########admin home #######
def boy_home(request):
    return render(request,'boy/index.html')
#############login #########################
def boy_login(request):  
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = User.objects.filter(username=uname).first()
        
        if user is not None and user.check_password(passw) and user.is_boy:
            login(request, user)
            return redirect('boy_home')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, "boy/login.html")

def boy_order_view(request):  
    order = CheckoutItem.objects.filter(boys=request.user)
    context={
        'order':order,
    }
    return render(request, "boy/order.html",context)

def assign_boys_work(request, pk):
    # Retrieve the CheckoutItem using the provided primary key (pk)
    checkout_item = get_object_or_404(CheckoutItem, checkout_id=pk)
    

    if request.method == 'POST':
        # Get the selected boy and status from the form
     
        selected_status = request.POST.get('status')


        # Update the status if it's provided
        if selected_status:
            checkout_item.status = selected_status

        # Save the updated checkout item
        checkout_item.save()

        # Show a success message and redirect if needed
        messages.success(request, "Work assigned successfully.")
        return redirect('boy_order_view')  # Replace with your desired redirect view name

    context = {
        'checkout_item': checkout_item,
       
    }
    return render(request, 'boy/assign.html', context)

from django.shortcuts import render
from django.db.models import Count,Sum


def best_selling_pets(request):
    # Initialize context dictionary
    context = {
        'from_date': None,
        'to_date': None,
        'best_selling_package': None,
        'error': None
    }
    
    if request.method == 'GET':
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        
        # Ensure dates are valid
        if from_date and to_date:
            try:
                # Convert string dates to datetime objects
                from_date = timezone.datetime.strptime(from_date, '%Y-%m-%d')
                to_date = timezone.datetime.strptime(to_date, '%Y-%m-%d')
                
                # Filter CheckoutItem records by date range and aggregate
                best_selling_packages = CheckoutItem.objects.filter(
                    checkout__created_at__range=(from_date, to_date)
                ).values('product_name').annotate(
                    num_bookings=Count('id'),  # Count the occurrences
                    total_quantity=Count('quantity')  # Total quantity sold
                ).order_by('-num_bookings')  # Sort by the number of bookings
                
                # Get the top-selling pet
                context['best_selling_package'] = best_selling_packages.first() if best_selling_packages.exists() else None
            
            except ValueError:
                context['error'] = 'Invalid date format. Please use YYYY-MM-DD.'
        else:
            context['error'] = 'Please provide both from_date and to_date.'

        context['from_date'] = from_date
        context['to_date'] = to_date
        
        return render(request, 'admin/best_sell.html', context)
    
    return render(request, 'admin/best_sell.html', context)

def lowest_selling_pets(request):
    # Initialize context dictionary
    context = {
        'from_date': None,
        'to_date': None,
        'lowest_selling_package': None,
        'error': None
    }
    
    if request.method == 'GET':
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        
        # Ensure dates are valid
        if from_date and to_date:
            try:
                # Convert string dates to datetime objects
                from_date = timezone.datetime.strptime(from_date, '%Y-%m-%d')
                to_date = timezone.datetime.strptime(to_date, '%Y-%m-%d')
                
                # Filter CheckoutItem records by date range and aggregate
                lowest_selling_packages = CheckoutItem.objects.filter(
                    checkout__created_at__range=(from_date, to_date)
                ).values('product_name').annotate(
                    num_bookings=Count('id'),  # Count the occurrences
                    total_quantity=Sum('quantity')  # Total quantity sold
                ).order_by('num_bookings', 'total_quantity')  # Sort by least number of bookings
                
                # Get the lowest-selling pet
                context['lowest_selling_package'] = lowest_selling_packages.first() if lowest_selling_packages.exists() else None
            
            except ValueError:
                context['error'] = 'Invalid date format. Please use YYYY-MM-DD.'
        else:
            context['error'] = 'Please provide both from_date and to_date.'

        context['from_date'] = from_date
        context['to_date'] = to_date
        
        return render(request, 'admin/lowest_sell.html', context)
    
    return render(request, 'admin/lowest_sell.html', context)

def most_buying_users(request):
    # Initialize context dictionary
    context = {
        'from_date': None,
        'to_date': None,
        'top_buying_users': None,
        'error': None
    }
    
    if request.method == 'GET':
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        
        # Ensure dates are valid
        if from_date and to_date:
            try:
                # Convert string dates to datetime objects
                from_date = timezone.datetime.strptime(from_date, '%Y-%m-%d')
                to_date = timezone.datetime.strptime(to_date, '%Y-%m-%d')
                
                # Filter Checkout records by date range and aggregate by user
                top_buying_users = Checkout.objects.filter(
                    created_at__range=(from_date, to_date)
                ).values('user__name', 'user__email').annotate(
                    purchase_count=Count('id')  # Count the number of purchases per user
                ).order_by('-purchase_count')  # Sort by the highest number of purchases
                
                context['top_buying_users'] = top_buying_users
            
            except ValueError:
                context['error'] = 'Invalid date format. Please use YYYY-MM-DD.'
        else:
            context['error'] = 'Please provide both from_date and to_date.'

        context['from_date'] = from_date
        context['to_date'] = to_date
        
        return render(request, 'admin/most_buyer.html', context)
    
    return render(request, 'admin/most_buyer.html', context)

def view_user_profile(request,pk):
    view=User.objects.get(pk=pk,is_customer=True)
    context={
        'view':view
    }
    return render(request,'user/view_profile.html',context)

def update_user_profile(request,pk):
    update=User.objects.get(pk=pk,is_customer=True)
    if request.method == 'POST':
        if 'img' in request.FILES:
            if len(update.photo) > 0:
                os.remove(update.photo.path)
            update.photo = request.FILES['img']
        update.username=request.POST.get('username')
        update.name=request.POST.get('name')
        update.mobile=request.POST.get('mobile')
        
        update.email=request.POST.get('email') 
        update.Address=request.POST.get('address') 
        update.save()
        messages.success(request,"Update successfully")
        return redirect('view_user_profile',pk=update.pk)
    context={
        'update':update
    }
    return render(request,'user/update_profile.html',context)

######### search #############
from django.db.models import Q

def search_items(request):
    query = request.GET.get('search', '')

    pets = Pet.objects.filter(
        Q(name__icontains=query) |
        Q(age__icontains=query) |
        Q(color__icontains=query) |
        Q(price__icontains=query)
    )

    products = Products.objects.filter(
        Q(name__icontains=query) |
        Q(price__icontains=query)
    )

    context = {
        'pets': pets,
        'products': products,
        'query': query
    }
    return render(request, 'user/search_results.html', context)

def staff_login(request): 

    roles = User.objects.exclude(role__isnull=True).values('role')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        selected_role = request.POST.get('role')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if the role matches the user's role
           
            if user.is_staff and selected_role == "Stock Manager":
                login(request, user)
                return redirect('staff_home')
            elif user.is_boy and selected_role == "Delivery Boy":
                login(request, user)
                return redirect('boy_home')
            else:
                messages.error(request, 'Invalid role for this user.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request,'staff/login.html',{'roles': roles})


def pet_booking(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        holder_name = request.POST.get('holder_name')
        stock_count = int(request.POST.get('stock_count', 1))
        advance_amount = int(request.POST.get('advance_amount', 0))

        # Check if requested stock is available
        if stock_count > pet.stock_level:
            messages.error(request, "Insufficient stock available.")
            return redirect('pet_booking', pk=pk)

        # Calculate the balance amount
        total_price = pet.price * stock_count
        balance_amount = total_price - advance_amount

        # Save booking to Pet_book model
        pet_booking = Pet_book.objects.create(
            cust=request.user,
            pet=pet,
            stock=stock_count,
            holder_name=holder_name,
            ac_number=account_number,
            advance_amount=advance_amount,
            balance_amount=balance_amount,
        )

        # Update pet stock level
        pet.stock_level -= stock_count
        pet.save()

        return redirect('pet_success')  # Redirect to a success page after booking

    context = {'pet': pet}
    return render(request, 'user/book_pet.html', context)


def pet_success(request):
   
    return render(request,'user/pet_success.html')

def pet_history_view(request):
    user = request.user
    # Get all checkout items for the current user, ordered by the `created_at` field in the related Checkout model
    orders = Pet_book.objects.filter(cust=user).order_by('created_at')
    return render(request, 'user/pet_history.html', {'orders': orders})

