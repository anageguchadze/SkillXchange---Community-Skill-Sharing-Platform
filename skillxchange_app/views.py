from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Course, CustomUser, Enrollment, Review
from .serializers import CustomUserSerializer, CourseSerializer, EnrollmentSerializer, ReviewSerializer
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend


class CourseFilter(FilterSet):
    category = filters.CharFilter(field_name='category', lookup_expr='icontains')
    max_students = filters.NumberFilter(field_name='max_students')

    class Meta:
        model = Course
        fields = ['category', 'max_students']

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseFilter


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 'page_size'  
    max_page_size = 100