from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('rest_framework.urls', namespace='api')),
    path('admin/', admin.site.urls),
]

