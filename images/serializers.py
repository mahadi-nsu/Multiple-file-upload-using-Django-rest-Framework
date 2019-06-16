from rest_framework.serializers import (
    ModelSerializer
)

from .models import (
    Vehicle,
    Image
)

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class VehicleSerializer(ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = "__all__"