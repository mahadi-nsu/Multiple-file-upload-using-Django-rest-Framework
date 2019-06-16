from django.shortcuts import render

from rest_framework.parsers import MultiPartParser

from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView
)

from .models import (
    Vehicle,
    Image
)

from .serializers import (
    VehicleSerializer,
    ImageSerializer
)

class VehicleListCreateAPIView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        print(request.POST.get('name'))
        print(request.POST.get('description'))
        print(request.FILES.getlist('images'))
        
        for image in request.FILES.getlist('images'):
            Image.objects.create(
                name="something red",
                image=image,
                vehicle=Vehicle.objects.get(pk=1)
            )
        return Response()
