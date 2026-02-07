from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('whistle',views.whistles,name='whistle'),
    path('contact',views.contacts,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.login_view,name='login'),
    path('viewproduct/<int:id>/',views.products,name='viewproduct'),
    path('whistle/add/<int:id>/',views.add_to_whistle,name='add_to_whistle'),
    path('add_to_carts/<int:id>/',views.add_to_carts,name='add_to_carts'),
    path('success',views.success,name='success'),
    path('whistle/delete/<int:id>',views.whistledelete,name='deletewhistle')
]