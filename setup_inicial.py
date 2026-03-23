import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_fein.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

# Categorías
cat_tazas, _ = Category.objects.get_or_create(name='Tazas', slug='tazas')
cat_estuches, _ = Category.objects.get_or_create(name='Estuches', slug='estuches')
print("✅ Categorías creadas.")

productos = [
    {'category': cat_tazas, 'name': 'Taza Botanical Dreams', 'slug': 'taza-botanical-dreams', 'description': 'Taza de cerámica con diseño botánico de hojas y flores silvestres.', 'price': 5000},
    {'category': cat_tazas, 'name': 'Taza Luna y Mar', 'slug': 'taza-luna-y-mar', 'description': 'Diseño minimalista con luna y olas. Acabado mate en tonos azules y terracota.', 'price': 5000},
    {'category': cat_tazas, 'name': 'Taza Café con Letras', 'slug': 'taza-cafe-con-letras', 'description': 'Personalizada con tu nombre o frase favorita. Tipografía script sobre fondo crema.', 'price': 5000},
    {'category': cat_estuches, 'name': 'Estuche Wildflowers', 'slug': 'estuche-wildflowers', 'description': 'Estuche rígido con ilustración de flores silvestres. Compatible con iPhone y Samsung.', 'price': 3500},
    {'category': cat_estuches, 'name': 'Estuche Abstracto Terracota', 'slug': 'estuche-abstracto-terracota', 'description': 'Diseño abstracto en paleta terracota y crema. Textura mate anti-huellas.', 'price': 3500},
    {'category': cat_estuches, 'name': 'Estuche Nombre Custom', 'slug': 'estuche-nombre-custom', 'description': 'Crea tu propio estuche con tu nombre o inicial. Diseño exclusivo único.', 'price': 3500},
]
for p in productos:
    obj, created = Product.objects.get_or_create(slug=p['slug'], defaults=p)
    print(f"  {'✅' if created else '⏩'} {obj.name}")

# Usuarios
if not User.objects.filter(username='admin_fein').exists():
    User.objects.create_superuser(username='admin_fein', email='admin@fein.cl', password='fein2024admin')
    print("✅ Admin creado: admin_fein / fein2024admin")
else:
    print("⏩ Admin ya existe.")

if not User.objects.filter(username='cliente_fein').exists():
    User.objects.create_user(username='cliente_fein', email='cliente@fein.cl', password='fein2024cliente')
    print("✅ Cliente creado: cliente_fein / fein2024cliente")
else:
    print("⏩ Cliente ya existe.")

print("\n🎉 ¡Listo! Tienda Fein configurada.")
print("Admin:   admin_fein / fein2024admin")
print("Cliente: cliente_fein / fein2024cliente")
