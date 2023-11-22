from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment_stock/<int:product_id>/', increment_stock, name='increment_stock'),
    path('decrement_stock/<int:product_id>/', decrement_stock, name='decrement_stock'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete-item-ajax/<int:id>', delete_item_ajax, name='delete_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('get-user-products/', get_user_products, name='get_user_products'),
]