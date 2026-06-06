from django.contrib import admin
from django.urls import path, include
from dashboard.views import weather_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),

    path("api/weather/", weather_view),
]