from django.contrib.auth import login
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("checkout/", views.checkout, name="checkout"),
    path("contact/", views.contact, name="contact"),
    path("customer/", views.customer, name="customer"),
    path("payment/", views.payment, name="payment"),
    path("shop/", views.shop, name="shop"),
    path("single/", views.single, name="single"),
    path("login/", views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout")
]
