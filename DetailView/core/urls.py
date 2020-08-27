from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cbv.urls', namespace='cbv')),
    path('books/', include('books.urls', namespace='books')),
]
