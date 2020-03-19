from django.shortcuts import render

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
    
    return render(
        request,
        'index.html',
        context={
        	'num_books':num_books,
        	'num_instances':num_instances,
        	'num_instances_available':num_instances_available,
        	'num_authors':num_authors,
        	'fragment':'fragment',
        },
    )


def search_fragment(request):
	"""
	Searchs and displays books that include given fragment in their titles
	"""

	#str method find but returns True or False
	def find_bin(title, fragment):
		res = title.lower().find(fragment)
		if (res == -1):
			return False
		else:
			return True
	
	#gets POST data
	try:
		request.method == "POST"
	except:
		pass
	else:
		fragment = request.POST["fragment"]

	list_of_req_books = [book for book in Book.objects.all() if find_bin(book.title, fragment)]

	return render(
		request, 
		"src_frg.html", 
		context={
			"list_of_req_books":list_of_req_books,
			"fragment":fragment,
		}, 
	)
