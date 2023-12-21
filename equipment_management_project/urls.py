from django.urls import path, include  # Import 'path' and 'include'

urlpatterns = [
    # ... other paths ...
    path('equipment/', include('equipment_management_app.urls')),
    # Add other paths as needed
]
