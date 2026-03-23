from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import CartItem
from .models import Order, OrderItem


@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user).select_related('product')
    if not items.exists():
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('catalog')
    total = sum(item.subtotal() for item in items)
    total_formatted = f"${int(total):,}".replace(',', '.')
    return render(request, 'orders/checkout.html', {
        'items': items,
        'total': total,
        'total_formatted': total_formatted,
    })


@login_required
def order_confirm(request):
    if request.method != 'POST':
        return redirect('checkout')
    items = CartItem.objects.filter(user=request.user).select_related('product')
    if not items.exists():
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('catalog')
    total = sum(item.subtotal() for item in items)
    order = Order.objects.create(user=request.user, total=total)
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            product_name=item.product.name,
            price=item.product.price,
            quantity=item.quantity,
        )
    items.delete()
    messages.success(request, f'¡Pedido #{order.id} confirmado! 🎉')
    return redirect('order_detail', pk=order.pk)


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})
