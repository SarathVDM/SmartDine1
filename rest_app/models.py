# Create your models here.
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_chef = models.BooleanField(default=False)
    is_waiter = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()

    def __str__(self):
        return self.Name


class chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    Address = models.TextField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Experience = models.IntegerField()
    specialisation = models.CharField(max_length=100)


class waiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone_no = models.IntegerField()
    Address = models.TextField(max_length=100)
    Experience = models.IntegerField()


class food(models.Model):
    c = models.ForeignKey(chef, on_delete=models.CASCADE, null=True)
    w = models.ForeignKey(waiter, on_delete=models.CASCADE, null=True)
    custom = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    FoodName = models.CharField(max_length=100)
    pic = models.FileField(upload_to='pics')
    food_type = models.CharField(max_length=200)
    food_category = models.CharField(max_length=200)
    Price = models.IntegerField()
    food_status = models.IntegerField(default=0)
    waiter_status = models.IntegerField(default=0)
    order_status = models.IntegerField(default=0)
    delivered_status = models.IntegerField(default=0)


class incre_req(models.Model):
    ch = models.ForeignKey(chef, on_delete=models.CASCADE, null=True)
    incredients = models.TextField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    in_status = models.IntegerField(default=0)

class table(models.Model):

    Table_no = models.IntegerField()

    def __str__(self):
        return str(self.Table_no)

class Rtable(models.Model):

    Table_no = models.IntegerField()

    def __str__(self):
        return str(self.Table_no)

class food_order(models.Model):
    c = models.ForeignKey(chef, on_delete=models.CASCADE, null=True)
    w = models.ForeignKey(waiter, on_delete=models.CASCADE, null=True)
    custom = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    FoodName = models.CharField(max_length=100,null=True)
    food_type = models.CharField(max_length=200,null=True)
    table_no = models.IntegerField(default=0)
    phone = models.IntegerField(null=True)
    Price = models.IntegerField(null=True)
    cardnumber = models.IntegerField(null=True)
    cvv = models.IntegerField(null=True)
    date = models.DateField()
    food_status = models.IntegerField(default=0)
    waiter_status = models.IntegerField(default=0)
    order_status = models.IntegerField(default=0)
    pay_status = models.IntegerField(default=0)
    delivered_status = models.IntegerField(default=0)

class table_order(models.Model):
    c = models.ForeignKey(chef, on_delete=models.CASCADE, null=True)
    w = models.ForeignKey(waiter, on_delete=models.CASCADE, null=True)
    custom = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    table_no = models.ForeignKey(table, on_delete=models.CASCADE,null=True)
    date = models.DateField()
    time = models.TimeField()
    expected_time = models.TimeField()
    t_status = models.IntegerField(default=0)
    torder_status = models.IntegerField(default=0)
    tpay_status = models.IntegerField(default=0)
    tdelivered_status = models.IntegerField(default=0)
