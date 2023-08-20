from django.contrib import admin
from django.urls import path, include
from api.views import NewsViewSet, SpecificNewsAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', NewsViewSet.as_view()),
    path('api/v1/<int:id>', SpecificNewsAPI.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
