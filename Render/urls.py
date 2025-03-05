from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
]

admin.site.site_header = "Blog Management Admin"
admin.site.site_title = "Blog Management Portal"
admin.site.index_title = "Welcome to Blog Management System"