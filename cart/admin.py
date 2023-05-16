from django.contrib import admin
from .models import cart,cartitem
# Register your models here.
# class cartadmin(admin.ModelAdmin):
#     list_display = ['cart_id']
admin.site.register(cart)
admin.site.register(cartitem)

