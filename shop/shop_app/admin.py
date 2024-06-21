from django.contrib import admin

from shop_app.models import Category, Product, Store

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)