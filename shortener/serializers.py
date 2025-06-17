from rest_framework import serializers
from .models import ShortURL


class ShortenURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ["original_url"]
