from django.urls import path
from . import views
urlpatterns=[
   path('├žartDetails',views.cart_details,name='├žartDetails'),
   path('add/<int:product_id>/',views.add_cart,name='addcart'),

]