from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('producto/<slug:slug>/', views.product_detail, name='product_detail'),
    path('gestion/productos/', views.admin_products, name='admin_products'),
    path('gestion/productos/nuevo/', views.product_create, name='product_create'),
    path('gestion/productos/<int:pk>/editar/', views.product_edit, name='product_edit'),
    path('gestion/productos/<int:pk>/eliminar/', views.product_delete, name='product_delete'),
]
