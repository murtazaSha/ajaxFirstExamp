
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="indexs"),
    path('likepost/', views.likePost, name="postLikes"),
]
