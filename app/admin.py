from django.contrib import admin
from .models import Customer, Product, OrderPlaced, CART, ChatLinks

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderPlaced)
admin.site.register(CART)
admin.site.register(ChatLinks)
