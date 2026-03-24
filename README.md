# Tienda Fein
![Tienda Fein](media/products/20260227_004614.jpg)

Tienda Fein es una aplicación web de comercio electrónico desarrollada con Django. Permite a los usuarios navegar por productos, agregar items al carrito, realizar pedidos y gestionar cuentas de usuario. Incluye panel de administración para gestionar productos.

## ✨ Características Principales

- **Catálogo de Productos**: Vista de productos por categoría, detalle individual, búsqueda y filtros.
- **Carrito de Compras**: Agregar/eliminar items, contador en navbar.
- **Sistema de Pedidos**: Checkout con detalles de pedido, historial de órdenes.
- **Autenticación**: Login/logout de usuarios.
- **Panel Admin**: Gestión CRUD de productos, categorías, órdenes.
- **Imágenes de Productos**: Soporte para upload y visualización.
- **Responsive**: Plantillas con CSS personalizado (`fein.css`).

## 🛠️ Tecnologías

- **Backend**: Django 4.2+
- **Base de Datos**: SQLite (producción: configurable)
- **Frontend**: HTML/CSS/JS + Bootstrap (implícito en templates)
- **Librerías**: Pillow (imágenes)
- **Idioma**: Español (Chile)

## 🚀 Instalación Rápida

1. **Clonar/Descargar** el proyecto.
2. **Entorno Virtual** (recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
3. **Instalar Dependencias**:
   ```
   pip install -r requirements.txt
   ```
4. **Migraciones**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Crear Superusuario** (opcional):
   ```
   python manage.py createsuperuser
   ```
6. **Cargar Datos Iniciales** (si existe):
   ```
   python setup_inicial.py
   ```
7. **Ejecutar Servidor**:
   ```
   python manage.py runserver
   ```
   Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📁 Estructura del Proyecto

```
tienda_fein/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── media/          # Imágenes de productos
├── static/         # CSS (fein.css)
├── templates/      # base.html
├── accounts/       # Login/Registro
├── cart/           # Carrito y context_processor
├── orders/         # Pedidos y checkout
├── store/          # Productos, catálogo, admin
└── tienda_fein/    # Configuración Django
    ├── settings.py
    └── urls.py
```

## 👥 Acceso

- **Sitio Público**: `/` (catálogo)
- **Admin**: `/admin/` (superusuario)
- **Login**: `/accounts/login/`
- **Carrito**: `/cart/`
- **Órdenes**: `/orders/`

## 📸 Capturas

- [Catálogo](store/templates/store/catalog.html)
- [Detalle Producto](store/templates/store/product_detail.html)
- [Carrito](cart/templates/cart/cart_detail.html)
- [Checkout](orders/templates/orders/checkout.html)

## 🔧 Configuración Adicional

- **Producción**: Cambiar `DEBUG=False`, configurar `ALLOWED_HOSTS`, usar PostgreSQL/MySQL.
- **Emails**: Configurar en `settings.py` para notificaciones.
- **Pagos**: Extensible para Stripe/MercadoPago.

## 🤝 Contribuir

1. Fork del repositorio.
2. Crear branch `feature/xxx`.
3. Commit changes.
4. Pull Request.

## 📄 Licencia

MIT License - ver `LICENSE` (agregar si necesario).

¡Gracias por usar Tienda Fein! 🛒✨
