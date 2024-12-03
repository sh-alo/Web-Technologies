from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.index, name="books.index"),  # Homepage
    path('list_books/', views.list_books, name="books.list_books"),  # List of books
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),  # View a single book
    path('aboutus/', views.aboutus, name="books.aboutus"),  # About page
]


