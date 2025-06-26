from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from .models import ShortURL
from .serializers import ShortenURLSerializer
from .utils import create_short_url


class ShortenURLView(APIView):
    @extend_schema(request=ShortenURLSerializer, responses={200: dict})
    def post(self, request):
        serializer = ShortenURLSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        original_url = serializer.validated_data["original_url"]
        obj = create_short_url(original_url)
        short_url = request.build_absolute_uri(f"/short/{obj.short_code}")
        return Response({"short_url": short_url})


class ExpandURLView(APIView):
    def get(self, request, code):
        obj = get_object_or_404(ShortURL, short_code=code)
        return Response({"original_url": obj.original_url})
