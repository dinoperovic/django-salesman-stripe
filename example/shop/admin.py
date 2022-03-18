from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
