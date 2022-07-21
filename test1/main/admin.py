from django.contrib import admin
from .models import Maktab, Talaba
# Register your models here.

@admin.register(Maktab)
class MaktabAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'maktab', 'sinf_raqam', 'add_time']