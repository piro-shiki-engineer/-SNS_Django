from django.urls import path
from .views import signup_func, login_func, logout_func, list_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
    path('list/', list_func, name='list'),
    path('logout', logout_func, name='logout'),
]
