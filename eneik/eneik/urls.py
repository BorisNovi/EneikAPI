from django.contrib import admin
from django.urls import path, include
from api.views import NewsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/', NewsViewSet.as_view()),
    # path('api/v1/<int:id>', SpecificNewsAPI.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
