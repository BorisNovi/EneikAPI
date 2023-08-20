from .models import News
from .serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import (
    views,
    viewsets,
    permissions,
    generics,
)


class NewsAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'data': serializer.data
        })


class SpecificNewsAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_url_kwarg = 'id'
