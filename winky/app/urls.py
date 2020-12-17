from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('login/movies', movies, name='movies'),
    path('login/movies/wishlist', add_to_wish_list, name='add_to_wish_list'),
    ]
