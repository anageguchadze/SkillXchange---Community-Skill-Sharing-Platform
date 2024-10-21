from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, CourseViewSet, EnrollmentViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]