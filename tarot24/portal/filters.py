from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from django import forms

from .models import Post, Author

class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        lookup_expr='iregex',
        label='Заголовок'
    )
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор'
    )
    time_publication = DateFilter(
        field_name= 'time_publication',
        lookup_expr='gt',
        widget=forms.DateInput(attrs={'type':'date'}),
        label='Дата'
    )
