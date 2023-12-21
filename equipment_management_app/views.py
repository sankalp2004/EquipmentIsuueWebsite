# views.py
from django.shortcuts import render, redirect
from .models import Equipment
from .forms import TransactionForm

def issue_equipment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            equipment = transaction.equipment
            equipment.quantity -= 1
            equipment.save()
            return redirect('issue_equipment')  # Redirect to the same page after issuing equipment
    else:
        form = TransactionForm()

    return render(request, 'inventory/issue_equipment.html', {'form': form})


def return_equipment(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            equipment = transaction.equipment
            equipment.quantity += 1  # Increment quantity when equipment is returned
            equipment.save()
            return redirect('return_equipment')  # Redirect after returning equipment
    else:
        # Filter available equipment for the form
        available_equipment = Equipment.objects.filter(quantity__gt=0)
        form = TransactionForm()
        form.fields['equipment'].queryset = available_equipment  # Set queryset for the equipment field

    return render(request, 'inventory/return_equipment.html', {'form': form})
