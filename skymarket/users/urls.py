from django.conf.urls.static import static
from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from skymarket import settings

user_routers = SimpleRouter()
user_routers.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(user_routers.urls)),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
