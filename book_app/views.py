from django.shortcuts import render
from django.db.models import Max, Min, Avg, Count, Sum, F,ExpressionWrapper,IntegerField

from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView

from .models import Book, Author, Publisher, Store

#https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-date-based/

class HomePageView(TemplateView):
    template_name = 'book_app/home.html'

class AuthorList(ListView):
    model = Author
    template_name = 'book_app/author.html'
    context_object_name = 'authors'

class AuthorDetail(DetailView):
    model = Author 
    template_name = 'book_app/author_detail.html'
    context_object_name = 'author'

class BookList(ListView):
    model = Book
    template_name = 'book_app/books.html'
    context_object_name = 'books'

class BookDetail(DetailView):
    model = Book
    template_name = 'book_app/books_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookDetail,self).get_context_data(**kwargs)
        context['book_total'] = Book.objects.filter(pk=self.kwargs.get('pk')).aggregate(
           book_total=Sum('price') + Sum('price') 
        )
        return context


class PublisherList(ListView):
    model = Publisher
    template_name = 'book_app/publishers.html'
    context_object_name = 'publishers'

class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'book_app/publishers_detail.html'
    context_object_name = 'publisher'

class StoreList(ListView):
    model = Store 
    template_name = 'book_app/stores.html'
    context_object_name = 'stores'

class StoreDetail(DetailView):
    model = Store 
    template_name = 'book_app/stores_detail.html'
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        context = super(StoreDetail,self).get_context_data(**kwargs)
        #context['book_list'] = Store.objects.filter(pk=self.kwargs.get('pk')).annotate(min_price=Min('books__price'), max_price=Max('books__price'))
        context['book_list'] = Store.objects.filter(pk=self.kwargs.get('pk')).aggregate(
            min_price=Min('books__price'),
            max_price=Max('books__price'),
            avg_price=Avg('books__price'),
            total_pages=Sum('books__pages'),
            first_publish=Min('books__pubdate'),
            last_publish=Max('books__pubdate'),
        )
        #aggregate(average_rating=Avg('book__rating'))
        return context

