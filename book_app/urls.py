from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('author/', views.AuthorList.as_view(), name='author'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('books/', views.BookList.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('publishers/', views.PublisherList.as_view(), name='publishers'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
    path('stores/', views.StoreList.as_view(), name='stores'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='store_detail'),
]