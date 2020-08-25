from django.urls import include, path, re_path
from .views import Home, upload, book_list, upload_book, delete_book, \
    BookListView, UploadBookView

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('upload/', upload, name='upload'),
    path('books/', book_list, name='book_list'),
    path('books/upload/', upload_book, name='upload_book'),
    path('books/<int:pk>/', delete_book, name='delete_book'),

    path('class/books/', BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', UploadBookView.as_view(), name='class_upload_book'),
]
