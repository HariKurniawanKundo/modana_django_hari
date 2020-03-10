from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "users"

router = routers.DefaultRouter()
router.register(r"lists", views.UserViewSet, basename='User')

urlpatterns = [
    path("", include(router.urls)),
]
