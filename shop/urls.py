from django.urls import path
from . import views
#from django.contrib import admin
urlpatterns=[
    #path('admin/',admin.site.urls),
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search')

]