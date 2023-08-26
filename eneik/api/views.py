from .models import News
from .serializers import NewsSerializer
from rest_framework import (
    permissions,
    viewsets,
)


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            start = int(self.request.GET.get('start', 0))
            count = int(self.request.GET.get('count', 20))
            return News.objects.filter(pk__gte=start)[:count]

        return News.objects.filter(pk=pk)
