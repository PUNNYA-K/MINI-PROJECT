from django.urls import path
from . import views
urlpatterns = [
    path('cus_home', views.index, name='index'),
############admin#######
    path('adm_home', views.adm_home, name='adm_home'),
    path('admin_register', views.admin_register, name='admin_register'),
    
    path('admin_login', views.admin_login, name='admin_login'),
    path('staff_register', views.staff_register, name='staff_register'),
    path('delete_staff/<int:pk>/', views.delete_staff, name='delete_staff'),
    path('boy_register', views.boy_register, name='boy_register'),
    path('delete_boy/<int:pk>/', views.delete_boy, name='delete_boy'),
    path('add_category', views.add_category, name='add_category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('Logout', views.Logout, name='Logout'),
    path('update_staff/<int:pk>/', views.update_staff, name='update_staff'),
    path('update_boy/<int:pk>/', views.update_boy, name='update_boy'),
    
    path('all_order_history_view', views.all_order_history_view, name='all_order_history_view'),
    path('assign_work/<int:pk>/', views.assign_work, name='assign_work'),
    
    path('add_pet_category', views.add_pet_category, name='add_pet_category'),
    path('delete_pet_category/<int:pk>/', views.delete_pet_category, name='delete_pet_category'),

    #####staff####
    path('staff_login', views.staff_login, name='staff_login'),

    path('staff_home', views.staff_home, name='staff_home'),
    path('add_pet', views.add_pet, name='add_pet'),
    path('update_pet/<int:pk>/', views.update_pet, name='update_pet'),
    path('delete_pet/<int:pk>/', views.delete_pet, name='delete_pet'),

    path('add_product', views.add_product, name='add_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    #####cus####

    path('', views.cus_home, name='cus_home'),
    path('cus_login', views.cus_login, name='cus_login'),
    path('cus_register', views.cus_register, name='cus_register'),
    path('pet_details', views.pet_details, name='pet_details'),
    path('pet_details/<int:pk>/', views.pet_details, name='pet_details'),

    path('product_details<int:pk>', views.product_details, name='product_details'),
    path('pet_full_details<int:pk>', views.pet_full_details, name='pet_full_details'),

    path('add-to-cart/product/<int:product_id>/', views.add_to_cart, name='add_to_cart_product'),
    path('add-to-cart/pet/<int:pet_id>/', views.add_to_cart, name='add_to_cart_pet'),
    path('cart/', views.cart_detail, name='cart_detail'),

    path('cart/increase_quantity/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease_quantity/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    

    path('checkout', views.checkout_view, name='checkout'),
    path('checkout-success/', views.checkout_success, name='checkout-success'),
    path('order_history_view', views.order_history_view, name='order_history_view'),
    
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),

    path('pet_booking/<int:pk>/', views.pet_booking, name='pet_booking'),
    #####boys####

    path('boy_login', views.boy_login, name='boy_login'),
    path('boy_home', views.boy_home, name='boy_home'),
    path('boy_order_view', views.boy_order_view, name='boy_order_view'),
    path('assign_boys_work/<int:pk>/', views.assign_boys_work, name='assign_boys_work'),
    
    path('best_selling_pets', views.best_selling_pets, name='best_selling_pets'),
    path('lowest_selling_pets', views.lowest_selling_pets, name='lowest_selling_pets'),
    
    path('most_buying_users', views.most_buying_users, name='most_buying_users'),
    path('view_user_profile/<int:pk>/', views.view_user_profile, name='view_user_profile'),
    path('update_user_profile/<int:pk>/', views.update_user_profile, name='update_user_profile'),

    path('search_items/', views.search_items, name='search_items'),
    
    path('pet_success', views.pet_success, name='pet_success'),
    path('pet_history_view', views.pet_history_view, name='pet_history_view'),
    
    path('all_pet_history_view', views.all_pet_history_view, name='all_pet_history_view'),
    
    path('product_payment', views.product_payment, name='product_payment'),
    path('pet_payment', views.pet_payment, name='pet_payment'),

    path('sales_report', views.sales_report, name='sales_report'),
    
    

    

]