from rest_framework import viewsets
from . import models
from . import serializers

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    queryset = queryset+"oooo"
    serializer_class = serializers.BookSerializer

