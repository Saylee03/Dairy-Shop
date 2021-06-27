from django.shortcuts import render, redirect
from .models import Product, ProductCategory, Shop, WeekDay
from django.contrib.auth import authenticate, login, logout


def index(request):
    products = Product.objects.all()
    context={
        "products":products
    }
    return render(request, "index.html",context)
 

def about(request):
    return render(request, "about.html")


def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")


def customer(request):
    return render(request, "customer.html")


def payment(request):
    return render(request, "payment.html")


def shop(request):
    context={
        "user":None
    }
    return render(request, "index.html",context)


def single(request):
    
    product = Product.objects.get(title="Amul Milk")
    context = {
        'product': product,
        'product_quantity': range(1, product.quantity+1)
    }

    return render(request, "single.html", context)


def check_login(request):
    return render(request, "check.html")


def my_login(request):
    return render(request, "my-login.html")


def add_product(request):
    if request.user.is_authenticated:
        print(request.user.id)
        try:
            shop = Shop.objects.get(user=5)
            # request.user.id
            print("I am here 1")
            if request.method == 'POST':
                print("I am here 2")
                product = Product.objects.create(
                    title=request.POST.get('title'),
                    desc=request.POST.get('desc'),
                    mrp=request.POST.get('mrp'),
                    rate=request.POST.get('rate'),
                    discount=request.POST.get('discount'),
                    quantity=request.POST.get('quantity'),
                    information=request.POST.get('information'),
                    options=request.POST.get('options'),
                )
                print("I am here 3")
                for opt in request.POST.getlist('opts[]'):
                    opt_product = Product.objects.get(id=opt)
                    product.options.add(opt_product)
                    opt_product.options.add(product)
                print("I am here 4")
                ProductCategory.objects.get(
                    id=request.POST.get('category')).products.add(product)
            print("I am here 2")
            products = shop.products
            print("I am here 3")
            product_categories = shop.productCategories
            print("I am here 4")
            context = {
                'products': products,
                'product_categories': product_categories,
            }
            return render(request, "seller/new-product.html", context)
        except:
            return redirect("/seller-activation/")
    else:
        return redirect("/seller-login/")


def add_product_category(request):
    if request.user.is_authenticated:
        try:
            shop = Shop.objects.get(user=request.user.id)
            if request.method == 'POST':
                ProductCategory.objects.create(
                    name=request.POST.get('name'),
                    shop=shop
                )
            return render(request, "seller/add-product-category.html")
        except:
            return redirect("/seller-activation")
    else:
        return redirect("/seller-login/")


def seller_activation(request):
    if request.user.is_authenticated:
        try:
            Shop.objects.get(user=request.user.id)
            return redirect('/add-product/')
        except:
            if request.method == 'POST':
                shop = Shop.objects.create(
                    user=request.user,
                    name=request.POST.get('shop'),
                    openingTime=request.POST.get('start_time'),
                    closingTime=request.POST.get('end_time'),
                )
                for off_day in request.POST.getlist('off_days[]'):
                    shop.offDays.add(WeekDay.objects.get(id=off_day))
                return redirect('/add-product/')
            else:
                weekDays = WeekDay.objects.all()
                context = {
                    'weekdays': weekDays
                }
                return render(request, "seller/activation.html", context)

    else:
        return redirect("seller/login/")


def seller_login(request):
    if request.user.is_authenticated:
        try:
            Shop.objects.get(user=request.user.id)
            return redirect('/add-product/')
        except:
            return render(request, 'seller/activation.html')
    else:
        return render(request, "seller/login.html")


def login_view(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        context = {
        'user': user
        }

        return render(request, "index.html", context)
    else:
        redirect(my_login)

def logout_view(request):
    logout(request)
    context={
        "user":None
    }
    return render(request, "index.html",context)
 