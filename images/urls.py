from .views import (
    VehicleListCreateAPIView
)

from django.urls import path


app_name = "images"

urlpatterns = [
    path('vehicle/', VehicleListCreateAPIView.as_view(), name="vehicle-list-create")
]