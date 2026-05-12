# Cart
path('cart/', views.cart_detail, name='cart_detail'),
path('cart/add/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
path('cart/remove/<uuid:item_id>/', views.remove_from_cart, name='remove_from_cart'),
path('cart/update/<uuid:item_id>/', views.update_cart_item, name='update_cart_item'),