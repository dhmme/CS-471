from django.shortcuts import render
#from django.http import HttpResponse
#name = request.GET.get("name") or "world!"
def index(request):
    name = request.GET.get("name") or "Abdulrhman!" 
    return render(request, "bookmodule/index.html" , {"name": name})

def index2(request, val1 = 0):
    return render("value1 = "+str(val1)) 


def index(request):
    return render(request, "bookmodule/index.html") 
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')  

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')  

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html') 

def html5(request):

    return render(request, 'bookmodule/html5.html')


def links(request):

    return render(request, 'bookmodule/links.html')

def viewFormat(request):

    return render(request, 'bookmodule/formating.html')


def viewListing(request):

    return render(request, 'bookmodule/listing.html')


def viewTable(request):

    return render(request, 'bookmodule/tables.html')







def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)




# Create your views here.
