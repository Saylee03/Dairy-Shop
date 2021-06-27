from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=50, default="")
    desc = models .TextField()
    mrp = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    rate = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    information = models.TextField()
    options = models.ManyToManyField('self', blank=True)

    def images(self):
        return ProductImage.objects.filter(product=self)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='NewProduct_image', max_length=100)

    def __str__(self):
        return self.product.title + "image"


class WeekDay(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    oneline = models.CharField(max_length=100)
    shortDescription = models.TextField()
    longDescription = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    openingTime = models.TimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    closingTime = models.TimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    offDays = models.ManyToManyField(WeekDay)

    def productCategories(self):
        return ProductCategory.objects.filter(shop=self)

    def products(self):
        return Product.objects.filter(Productcategory__shop=self)

    def images(self):
        return ShopImage.objects.filter(shop=self)

    def __str__(self):
        return self.name


class ShopImage(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop_image',
                              height_field=200, width_field=200, max_length=100)

    def __str__(self):
        return self.shop.name + "image"


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_category_image',
                              height_field=200, width_field=200, max_length=100)

    def __str__(self):
        return self.name + " ( " + self.shop.name + " ) "


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unitPrice = models.DecimalField(max_digits=20, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=20, decimal_places=2)
