from django.views import generic

from .models import Book


class BookListView(generic.ListView):
	model = Book
	context_object_name = 'books_list'
	template_name = 'books/book_list.html'
