from django.urls import path

from shop_app import views

urlpatterns =[
    path('',views.show_shops,name='home'),
    path('add_store',views.add_shop,name='add_shop'),
    path('shop_delete/<int:pk>/',views.shop_delete,name='shop_delete'),
    path('shop_edit/<int:pk>/',views.shop_edit,name='shop_edit'),
    path('categories/', views.show_categories,name='categories'),
    path('category_add',views.category_add,name='category_add'),
    path('category_edit/<int:pk>/',views.category_edit,name='category_edit'),
    path('category_delete/<int:pk>/',views.category_delete,name='category_delete'),
    path('product_edit/<int:pk>/',views.product_edit,name='product_edit'),
    path('products/', views.show_products,name='products'),
    path('product_add', views.product_add,name='product_add'),
    path('product_delete/<int:pk>/', views.product_delete,name='product_delete'),
    path('shop_search/', views.shop_search, name='shop_search'),
    path('store_detail/<int:pk>/', views.store_detail, name='store_detail'),


]