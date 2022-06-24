from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_start, name='start'),
    path('tabs', views.index_tab, name='main'),
    path('books', views.index, name='home'),
    path('book/<int:id>/view', views.book_view, name='book_view'),
    path('book/new', views.book_new, name='book_new'),
    path('book/<int:id>/edit', views.book_edit, name='book_edit'),
    path('book/<int:id>/delete', views.book_delete, name='book_delete'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]