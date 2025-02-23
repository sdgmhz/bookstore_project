from django.views import generic
from django.urls import reverse_lazy

from .models import Book


class BookListView(generic.ListView):
	model = Book
	paginate_by = 2
	context_object_name = 'books'
	template_name = 'books/book_list.html'


class BookDetailView(generic.DetailView):
	model = Book
	# context_object_name = 'book'
	template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
	model = Book
	fields = '__all__'
	template_name = 'books/book_create.html'
	# success_url = reverse_lazy('book_list')


class BookUpdateView(generic.UpdateView):
	model = Book
	fields = ['title', 'author', 'description', 'price', 'cover']
	template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
	model = Book
	template_name = 'books/book_delete.html'
	success_url = reverse_lazy('book_list')





