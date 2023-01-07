from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViews

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('', StudentViews, basename="student-views")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('student/', include(router.urls)),
]