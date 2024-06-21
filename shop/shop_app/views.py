from django.shortcuts import render, redirect, get_object_or_404

from shop_app.forms import StoreForm, CategoryForm, ProductForm
from shop_app.models import Product, Category, Store


# Create your views here.


def home(request):
    return render(request, 'shop_app/home.html')


def shop_search(request):
    query = request.GET.get('q')
    shops = []
    if query:
        shops = Store.objects.filter(name__icontains=query)

    ctx = {
        'shops': shops,
    }
    return render(request, 'shop_app/shop_search.html', ctx)


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)

    ctx = {
        'store': store,
    }
    return render(request, 'shop_app/store_detail.html', ctx)

def show_shops(request):
    shops= Store.objects.all()
    ctx = {
        'shops': shops,

    }
    return render(request, 'shop_app/home.html', ctx)
def add_shop(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoreForm()
    ctx = {
        'form': form,
    }
    return render(request, 'shop_app/add_shop.html', context=ctx)
def shop_delete(request, pk):
    shop = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        shop.delete()
        return redirect('home')
    ctx = {
        'shop':shop
    }
    return render(request, 'shop_app/shop_delete.html', context=ctx)
def shop_edit(request, pk):
    shop = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoreForm(instance=shop)
    ctx = {
        'form': form,
    }
    return render(request, 'shop_app/shop_edit.html', context=ctx)




def show_categories(request):
    categories= Category.objects.all()
    ctx = {
        'categories': categories,

    }
    return render(request, 'shop_app/category.html', ctx)
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category', pk=pk)
    else:
        form = CategoryForm(instance=category)
    ctx ={
        'form': form,
    }
    return render(request, 'shop_app/category_edit.html', context=ctx)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category', pk=pk)
    ctx = {
        'category':category
    }
    return render(request, 'shop_app/category_delete.html', context=ctx)
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    ctx = {
        'form': form,
    }
    return render(request, 'shop_app/category_add.html', context=ctx)




def show_products(request):
    products= Product.objects.all()
    ctx = {
        'products': products,

    }
    return render(request, 'shop_app/products.html', ctx)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    ctx ={
        'form': form,
    }
    return render(request, 'shop_app/product_edit.html', context=ctx)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    ctx = {
        'form': form,
    }
    return render(request, 'shop_app/product_add.html', context=ctx)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products', pk=pk)
    ctx = {
        'product':product
    }
    return render(request, 'shop_app/product_delete.html', context=ctx)