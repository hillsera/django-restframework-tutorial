from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

from rest_framework import renderers

from snippets.views import api_root, SnippetViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]