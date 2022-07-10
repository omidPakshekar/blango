from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostList, PostDetail, UserDetail

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)