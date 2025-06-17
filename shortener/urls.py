from django.urls import path
from .views import ShortenURLView, ExpandURLView

urlpatterns = [
    path("shorten/", ShortenURLView.as_view(), name="shorten-url"),
    path("short/<str:code>/", ExpandURLView.as_view(), name="expand-url"),
]
