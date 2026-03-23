from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirmar/', views.order_confirm, name='order_confirm'),
    path('mis-pedidos/', views.order_list, name='order_list'),
    path('pedido/<int:pk>/', views.order_detail, name='order_detail'),
]
