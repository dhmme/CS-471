from django.urls import path 
from . import views
urlpatterns = [ 
path('', views.index), 
path('index2/<int:val1>/', views.index2),
path('<int:bookId>', views.viewbook) ,
path('', views.index, name= "books.index"), 
path('list_books/', views.list_books, name= "books.list_books"), 
path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
path('aboutus/', views.aboutus, name="books.aboutus"),
path('html5/', views.html5, name="books.html5"),
path('html5/links/', views.links, name="books.html5.links"),
path('html5/text/formatting', views.viewFormat, name="books.formatting"),
path('html5/listing/', views.viewListing, name="books.html5.listing"),
path('html5/tables/', views.viewTable, name="books.html5.tables"),
path('search/', views.search, name="books.search"),
path('bookList/', views.search, name="books.bookList"),
path('simple/query', views.simple_query, name="books.simple_query"),
path('complex/query', views.complex_query, name="books.complex_query"),
path('lab8/task1/', views.task1, name="books.lab8.task1"),
path('lab8/task2/', views.task2, name="books.lab8.task2"),
path('lab8/task3/', views.task3, name="books.lab8.task3"),
path('lab8/task4/', views.task4, name="books.lab8.task4"),
path('lab8/task5/', views.task5, name="books.lab8.task5"),
path('lab8/task7/', views.task7, name="books.lab8.task7"),

]