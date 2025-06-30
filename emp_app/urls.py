from rest_framework.schemas import get_schema_view
from django.urls import path
from .views import employee_search

urlpatterns = [
    path('search/', employee_search),
    path('openapi.json', get_schema_view(
        title="Employee Search API",
        description="OpenAPI schema for HR microservice",
        version="1.0.0"
    ), name='openapi-schema'),
]