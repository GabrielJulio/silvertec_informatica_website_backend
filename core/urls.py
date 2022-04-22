from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('api/', include('rest_framework.urls', namespace='api')),
    path('admin/', admin.site.urls),
]

