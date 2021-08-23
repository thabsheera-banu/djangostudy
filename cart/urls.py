from django.urls import path
from . import views
urlpatterns=[
   path('çartDetails',views.cart_details,name='çartDetails'),
   path('add/<int:product_id>/',views.add_cart,name='addcart'),

]