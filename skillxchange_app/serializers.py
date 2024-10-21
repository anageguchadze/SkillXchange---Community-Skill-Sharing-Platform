from rest_framework import serializers
from .models import CustomUser, Course, Enrollment, Review

class CustomUserSerializer(serializers. ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers. ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

        