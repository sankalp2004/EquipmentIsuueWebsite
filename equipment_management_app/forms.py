from django import forms
from django.shortcuts import render, redirect
from .models import Transaction

EQUIPMENT_CHOICES = [
    ('cricket_set_tennis', 'Cricket Set (Tennis)'),
    ('cricket_full_leather', 'Cricket Full Set (Leather Ball)'),
    ('football', 'Football'),
    ('volleyball', 'Volleyball'),
    ('badminton_set', 'Badminton Set'),
    ('basketball', 'Basketball'),
    ('tennis_set', 'Tennis Set'),
]

class TransactionForm(forms.ModelForm):
    equipment = forms.ChoiceField(choices=EQUIPMENT_CHOICES)
    borrower = forms.RegexField(
        regex=r'^225890\d{3}$',
        max_length=9,
        error_messages={
            'invalid': 'Enter a valid registration number (e.g., 225890XXX).'
        }
    )

    class Meta:
        model = Transaction
        fields = '__all__'


class ReturnTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['equipment', 'borrower', 'returned_date']
