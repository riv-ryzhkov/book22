from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Book
from django.forms import ModelForm, TextInput, Textarea, NumberInput
from django import forms
from django.utils.translation import gettext_lazy as _


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'short_text', 'text', 'published', 'count']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть автора'
            }),
            'short_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть короткий опис'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис'
            }),
            'published': TextInput(attrs={
                'class': 'col-xs-4',
                'id': 'ex1',
                'placeholder': 'Введіть рік видання'
            }),
            'count': NumberInput(attrs={
                'class': 'col-xs-2',
                'id': 'ex2',
                'placeholder': 'Введіть кількість книжок'
            })
        }


User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields=['username', 'email']