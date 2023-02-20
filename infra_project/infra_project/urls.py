from django.urls import path, include
from django.contrib import admin

# app_name = 'infra_app'

urlpatterns = [
    path("", include("infra_app.urls", namespace="infra_app")),
    path("admin/", admin.site.urls),
]
