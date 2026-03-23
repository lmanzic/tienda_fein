from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('cancelled', 'Cancelado'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    def __str__(self):
        return f"Orden #{self.id} - {self.user.username}"

    def total_formatted(self):
        return f"${int(self.total):,}".replace(',', '.')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product_name}"

    def subtotal(self):
        return self.price * self.quantity

    def subtotal_formatted(self):
        return f"${int(self.subtotal()):,}".replace(',', '.')
    