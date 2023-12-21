# admin.py
from django.contrib import admin
from .models import Equipment, Borrower, Transaction

admin.site.register(Equipment)
admin.site.register(Borrower)
admin.site.register(Transaction)
