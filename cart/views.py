from django.shortcuts import render, redirect
from shop.models import  *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def cart_details(request, tot=0, count=0, cart_items=None):
    try:
        ct_items=None     # ith Assign cheytheellel line 20 l Error Varum 
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quantity)
            count+=i.quantity
    except ObjectDoesNotExist:
        pass
    
    return render(request,'cart.html',{'ct':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id



def add_cart(request, product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quantity < c_items.prodt.stock:   # ivade quantity
            c_items.quantity+=1   # ivade quantity
        c_items.save()
    except items.DoesNotExist:   # ivade items
        c_items=items.objects.create(prodt=prod,quantity=1,cart=ct)  # ivade quantity
        c_items.save()
    return redirect('çartDetails')  # Ith Thettayirunnu




def min_cart(request):
    pass

def cart_delete(request):
    pass


