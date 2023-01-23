from django.urls import path
from . import views

urlpatterns = [
    path("",views.blog,name="starting-page" ),
    path("posts",views.post, name="posts-page"),
    path("post/<slug:slug>" ,views.post_details,name="post-details-page")
   ] 