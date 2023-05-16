from django.shortcuts import render, redirect, get_object_or_404
from shop.models import product
from .models import cart,cartitem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _cart_id(request):
     cart1=request.session.session_key
     if not cart1:
          cart1=request.session.create()
     return cart1

def add_cart(request,product_id):
     product1 = product.objects.get(id=product_id)
     try:
          cart1 = cart.objects.get(cart_id=_cart_id(request))

     except cart.DoesNotExist:
          cart1=cart.objects.create(cart_id=_cart_id(request))
          cart1.save()
     try:
          cart_item = cartitem.objects.get(prdts=product1,carts=cart1)
          if cart_item.quantity < cart_item.prdts.stock:
               cart_item.quantity += 1
          cart_item.save()
     except cartitem.DoesNotExist:
          cart_item = cartitem.objects.create(prdts=product1,quantity=1,carts=cart1)
          cart_item.save()
     return redirect('cart:cart_details')

def cart_details(request,total=0,counter=0,cart_items=None):
     try:
          cart1= cart.objects.get(cart_id=_cart_id(request))
          cart_items=cartitem.objects.filter(carts=cart1,active=True)
          for i in cart_items:
               total+=(i.prdts.price*i.quantity)
               counter+=i.quantity
     except ObjectDoesNotExist:
          pass
     return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def remove_cart(request,product_id):
     product1=get_object_or_404(product,id=product_id)
     cart1=cart.objects.get(cart_id=_cart_id(request))
     cart_item=cartitem.objects.get(prdts=product1,carts=cart1)
     if cart_item.quantity >1:
          cart_item.quantity -= 1
          cart_item.save()
     else:
          cart_item.delete()
     return redirect('cart:cart_details')

def full_remove(request,product_id):
     product1 = get_object_or_404(product, id=product_id)
     cart1 = cart.objects.get(cart_id=_cart_id(request))
     cart_item = cartitem.objects.get(prdts=product1, carts=cart1)
     cart_item.delete()
     return redirect('cart:cart_details')
