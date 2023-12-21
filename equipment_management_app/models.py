# models.py
from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Borrower(models.Model):
    name = models.CharField(max_length=100)
    # Add more fields like contact information, if needed

    def __str__(self):
        return self.name

class Transaction(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    returned_date = models.DateField(null=True, blank=True)

  
