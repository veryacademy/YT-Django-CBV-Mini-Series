from django.urls import path
from .views import IndexView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='ex2'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]
