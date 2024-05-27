from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage),
    path("books/", views.book_list),
    path("authors/", views.author_list),

    #GET
    path("api/books", views.Book_API),
    path("api/authors", views.Author_API),
    path("api/author_books", views.search_author_books),
    path("api/books/<int:pk>/update", views.update_book),
    path("api/books/<int:pk>", views.single_book),
    path("api/authors/<int:pk>", views.single_author),
    path("api/books/<int:pk>/delete", views.delete_book),
    path("api/authors/<int:pk>/delete", views.delete_author),

    #POST
    path("api/books/add", views.addBook),
    path("api/authors/add", views.addAuthor)
]