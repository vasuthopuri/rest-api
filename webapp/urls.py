from django.urls import path
from . import views

urlpatterns = [
    path(r'user/create/', views.UserCreateView.as_view(), name="user_create"),
    path(r'users/list/', views.UsersListView.as_view(), name="users_list"),
    path(r'users/(?P<pk>\d+)/detail/', views.UserDetailView.as_view(), name="user_detail"),
    path(r'users/(?P<pk>\d+)/update/', views.UserUpdateView.as_view(), name="user_update"),
   # path(r'users/(?P<pk>\d+)/delete/', views.UserDeleteView.as_view(), name="user_delete"),
]