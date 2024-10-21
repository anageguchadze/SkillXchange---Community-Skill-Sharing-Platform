# skillxchange_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CourseViewSet, EnrollmentViewSet, ReviewViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'reviews', ReviewViewSet)

# Define your URL patterns
urlpatterns = [
    path('', include(router.urls)),  # This will include all the routes created by the router
]
