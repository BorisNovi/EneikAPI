from .models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import (
    permissions,
    generics,
    mixins,
)


class NewsViewSet(generics.ListAPIView, mixins.CreateModelMixin):
    def get_queryset(self):
        start = int(self.request.GET.get('start', 0))
        count = int(self.request.GET.get('count', 20))
        return News.objects.filter(pk__gte=start)[:count]

    serializer_class = NewsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class SpecificNewsAPI(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
