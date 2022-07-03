from django.contrib import admin
from django.urls import path, include
import blog.views
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail"),
    path("ip/", blog.views.get_ip),
    path("__debug__/", include(debug_toolbar.urls)),


]
