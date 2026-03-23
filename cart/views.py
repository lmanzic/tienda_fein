from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Product
from .models import CartItem


@login_required
def cart_detail(request):
    items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum(item.subtotal() for item in items)
    total_formatted = f"${int(total):,}".replace(',', '.')
    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total': total,
        'total_formatted': total_formatted,
    })


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
        messages.success(request, f'Se agregó otra unidad de "{product.name}".')
    else:
        messages.success(request, f'"{product.name}" agregado al carrito 🛍️')
    return redirect(request.META.get('HTTP_REFERER', 'catalog'))


@login_required
def cart_update(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    if quantity <= 0:
        messages.error(request, 'La cantidad debe ser mayor a 0.')
    else:
        item.quantity = quantity
        item.save()
        messages.success(request, 'Carrito actualizado.')
    return redirect('cart_detail')


@login_required
def cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    messages.info(request, f'"{item.product.name}" eliminado del carrito.')
    return redirect('cart_detail')
