from django.contrib import admin
from .models import Product, ProductImage, Shop, ShopImage, ProductCategory, Cart

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Shop)
admin.site.register(ShopImage)
admin.site.register(ProductCategory)
admin.site.register(Cart)
