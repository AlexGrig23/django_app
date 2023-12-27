
from django.urls import path

from . import views


urlpatterns = [
    path('user_create/', views.UserCreateView.as_view(), name="user_create"),
    path('users_list/', views.UserListView.as_view(), name="users_list")

]
