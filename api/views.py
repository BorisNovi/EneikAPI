from .models import News
from .serializers import NewsSerializer
from django.db.models import F
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
            offset = int(self.request.GET.get('offset', 0))
            limit = int(self.request.GET.get('limit', 20))
            return News.objects.annotate(reverse_pk=F('pk')).order_by('-reverse_pk')[offset:offset+limit]

        return News.objects.filter(pk=pk)
