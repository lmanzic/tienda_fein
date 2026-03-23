from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm


def catalog(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    return render(request, 'store/catalog.html', {
        'products': products,
        'categories': categories,
        'current_category': current_category,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})


@staff_member_required
def admin_products(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'store/admin_products.html', {'products': products})


@staff_member_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto creado exitosamente!')
            return redirect('admin_products')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form, 'title': 'Nuevo Producto'})


@staff_member_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto actualizado!')
            return redirect('admin_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form, 'title': 'Editar Producto', 'product': product})


@staff_member_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('admin_products')
    return render(request, 'store/product_confirm_delete.html', {'product': product})
