from django.urls import path
from . import views
from .views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

#Пространство имен(помогает избежать ошибки при одинаковых именах маршрута)
app_name = 'library'

#В urlpatterns создаются и регестрируются маршруты
#Path это специальная функция которая позволяет регестрировать наш маршрут
urlpatterns = [
    #path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    #path('book_list/', views.book_list, name='book_list'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='books_create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    ]