"""mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import shop.views as shop_view


urlpatterns = [
    path('', include('shop.urls')),
    path('check_me/', shop_view.index),
    path('admin/', admin.site.urls),
    path('about', shop_view.about, name="about"),
    path('checkout', shop_view.checkout, name="checkout"),
    path('contact', shop_view.contact, name="contact"),
    path('customer', shop_view.customer, name="customer"),
    path('payment', shop_view.payment, name="payment"),
    path('shop', shop_view.shop, name="shop"),
    path('single', shop_view.single, name="single"),
    path('accounts/', include('allauth.urls')),
    path('check-login/', shop_view.check_login),
    path('my-login/', shop_view.my_login),
    path('add-product/', shop_view.add_product),
    path('seller-activation/', shop_view.seller_activation),
    path('seller-login/', shop_view.seller_login),
    path('add-product-category/', shop_view.add_product_category),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
