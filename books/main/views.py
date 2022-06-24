from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from faker import Faker
from random import randint



def index(request):
    books = Book.objects.all()
    # books = Book.objects.order_by('-id')
    # books = Book.objects.order_by('-id')[:4]
    # books = Book.objects.filter(author='ГОСТ')
    # books = Book.objects.filter(id__lt=0)
    numbers = len(Book.objects.all())
    return render(request, 'main/index.html', {'title': 'Книги', 'books': books, 'numbers': numbers})


def book_view(request, id=1):
    book = Book.objects.get(id=id)
    return render(request, 'main/book_view.html', {'title': 'Книги', 'book': book})


def index_tab(request):
    # books = Book.objects.all()
    # books = Book.objects.order_by('-id')[:10]
    books = Book.objects.order_by('-id')
    numbers = 'із ' + str(len(Book.objects.all()))
    return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})


def book_edit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(id=id)
            form = BookForm(instance=book)
        return render(request, 'main/book_edit.html', {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(id=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('main')

def book_delete(request, id=0):
    book = Book.objects.get(id=id)
    book.delete()
    # Book.save()
    # books = list(Book.objects.all())
    books = Book.objects.order_by('-id')
    numbers = 'із ' + str(len(Book.objects.all()))
    return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})



def book_new(request):
    b = Faker()
    b_new = Book.objects.create(
        title=b.company(),
        author=b.last_name(),
        text=' '.join(b.sentences(10)),
        short_text=' '.join(b.sentences()),
        published = str(b.year()),
        count=randint(1, 20)
    )
    b_new.save()
    # Book.save()
    # books = list(Book.objects.all())
    books = Book.objects.order_by('-id')[:10]
    numbers = '10 нових із ' + str(len(Book.objects.all()))
    return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})


def about(request):
    return render(request, 'main/about.html')
    # return render(request, 'main/start.html')

def index_start(request):
    return render(request, 'main/start.html')

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

