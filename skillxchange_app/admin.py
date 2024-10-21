from django.contrib import admin
from .models import CustomUser, Course, Enrollment, Review


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Review)
