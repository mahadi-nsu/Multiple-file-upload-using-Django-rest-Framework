from django.contrib import admin

# Register your models here.
from .models import (
    Vehicle,
    Image
)

admin.site.register(Vehicle)
admin.site.register(Image)