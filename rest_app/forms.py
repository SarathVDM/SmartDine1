import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, TimeInput

from .models import *


class UserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        exclude = ('user',)
        fields = ('Name', 'Phone_no')
class chefForm(forms.ModelForm):
    class Meta:
        model = chef
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address','Qualification','Experience','specialisation')


class waiterForm(forms.ModelForm):
    class Meta:
        model = waiter
        exclude = ('user',)
        fields = ('Name', 'Phone_no', 'Address','Experience')

class FoodForm(forms.ModelForm):
    class Meta:
        model = food
        fields = ('FoodName', 'pic', 'food_type','food_category','Price')

class TableForm(forms.ModelForm):
    class Meta:
        model = table
        fields = ('Table_no',)

class TablForm(forms.ModelForm):
    class Meta:
        model = Rtable
        fields = ('Table_no',)

class incredientsForm(forms.ModelForm):
    date = forms.DateField(required=True, widget=DateInput())

    time = forms.CharField(required=True, widget=TimeInput())

    class Meta:
        model =incre_req
        fields = ('incredients', 'date', 'time')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date

class DateInput(forms.DateInput):
    input_type = 'date'



class OrderForm(forms.ModelForm):
    date = forms.DateField(required=True, widget=DateInput())


    class Meta:
        model =food_order
        fields = ('FoodName', 'food_type','table_no', 'phone','Price','cardnumber','cvv','date')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date




class TimeInput(forms.TimeInput):
    input_type = 'time'

class TabForm(forms.ModelForm):
    date = forms.DateField(required=True, widget=DateInput())
    time = forms.CharField(required=True, widget=TimeInput())
    expected_time = forms.CharField(required=True, widget=TimeInput())

    class Meta:
        model =table_order
        fields = ('table_no', 'date', 'time', 'expected_time')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Invalid Date")
        return date