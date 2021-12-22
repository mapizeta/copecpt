from django.urls import path
from .import views

urlpatterns = [
    #path('', vie)
    path('create', views.userCreate, name="create"),
    path('update/<uuid:uuid>/', views.userUpdate, name="update"),
    path('detail/<uuid:uuid>/', views.userDetail, name="detail"),
    path('detail/', views.userDetail, name="detail"),
    path('delete/<uuid:uuid>/', views.userDelete, name="delete"),

]