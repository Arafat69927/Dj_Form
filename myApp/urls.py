from django.urls import path 
from myApp.views import * 
urlpatterns = [
    path('',product_view,name='product_view'),
    path('product_list/',product_list,name='product_list'),
    path('add_product/',add_product,name='add_product'),
    path('delete_product/<str:myid>',delete_product,name='delete_product'),
    path('edit_product/<str:myid>',edit_product,name='edit_product'),
]