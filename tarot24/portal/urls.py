from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, category_list, subscribe

# http://:127.0.0.1:8000/post/

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('article/create/', PostCreate.as_view(), name='article_create'),
    path('article/<int:pk>/update/', PostUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),

    path('cart/create/', PostCreate.as_view(), name='cart_create'),
    path('cart/<int:pk>/update/', PostUpdate.as_view(), name='cart_update'),
    path('cart/<int:pk>/delete/', PostDelete.as_view(), name='cart_delete'),
    path('category_list/', category_list, name='category_list'),
    path('subscribe/<int:pk>/', subscribe, name='subscribe'),
]
