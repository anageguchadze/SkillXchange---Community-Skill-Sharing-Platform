# skillxchange_pro/urls.py
from django.contrib import admin
from django.urls import path, include
from .yasg import schema_view  # Import from yasg.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('skillxchange_app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Optional ReDoc UI
]
