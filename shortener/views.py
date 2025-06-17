from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from .models import ShortURL
from .serializers import ShortenURLSerializer
from .utils import generate_code


class ShortenURLView(APIView):
    @extend_schema(request=ShortenURLSerializer, responses={200: dict})
    def post(self, request):
        serializer = ShortenURLSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data["original_url"]
            obj, created = ShortURL.objects.get_or_create(original_url=original_url)
            if created:
                obj.short_code = generate_code()
                obj.save()
            short_url = request.build_absolute_uri(f"/short/{obj.short_code}")
            return Response({"short_url": short_url})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpandURLView(APIView):
    def get(self, request, code):
        obj = get_object_or_404(ShortURL, short_code=code)
        return Response({"original_url": obj.original_url})
