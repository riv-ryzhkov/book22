from django.db import models
from django.contrib.auth.models import AbstractUser


# class User1(AbstractUser):
#     pass


class Book(models.Model):
    title = models.CharField('Назва', max_length=50, default='title')
    author = models.CharField('Автор', max_length=50, default='author')
    text = models.TextField('Опис', default='Long text')
    short_text = models.CharField('Короткий опис', max_length=100, default='short text')
    published = models.CharField('Рік видання', max_length=4, default='2022')
    count = models.IntegerField('Кількість', default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
