from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("loginPage/", views.loginPage, name="loginPage"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
    path('itemsPage/<str:section>/', views.itemsPage, name='itemsPage'),
    path('managePage/', views.managePage, name='managePage'),
    path('addRestaurant/', views.add_restaurant, name='addRestaurant'),
    path('addItem/', views.add_item, name='addItem'),
    path('editItem/<int:item_id>/', views.edit_item, name='editItem'),
    path('search/', views.search, name='search'),
]

