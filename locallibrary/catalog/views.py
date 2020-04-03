from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import *
# Create your views here.

from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    Displays main page of the site
    """
    # Number of all books
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Number of avaliable books
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context=context, )

class BookListView(generic.ListView):
    """
    Displays list of avaliable books
    """
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    """
    Displays detail information about a book
    """
    model = Book

class AuthorListView(generic.ListView):
    """
    Displays list of authors
    """
    model = Author
    paginate_by = 5

class AuthorDetailView(generic.DetailView):
    """
    Displays detail informaion about an author
    """
    model = Author