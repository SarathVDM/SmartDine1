import django_filters
from .models import food
from django import forms
from django_filters import CharFilter, filters


class FoodFilter(django_filters.FilterSet):
    food_category = CharFilter(field_name='food_category', label="Search by food category ",lookup_expr='icontains',widget=forms.TextInput(attrs={
            'placeholder': 'Search Names', 'class':'form-control'}))

    class Meta:
        model = food
        fields = ('food_category',)
