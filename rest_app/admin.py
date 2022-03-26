from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from . import models
from .models import User
admin.site.register(User)
admin.site.register(models.food)
admin.site.register(models.customer)
admin.site.register(models.food_order)