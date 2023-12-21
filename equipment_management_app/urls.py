from django.urls import path
from . import views  

urlpatterns = [
    path('issue_equipment/', views.issue_equipment, name='issue_equipment'),
    path('return_equipment/', views.return_equipment, name='return_equipment'),
    # Add other URLs as needed
]
