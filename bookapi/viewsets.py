from rest_framework import viewsets
from . import models
from . import serializers

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    
    dict = {"status_code": 200, "status": "success", "data": queryset}
    print("++++++++++++++")
    queryset = dict
    serializer_class = serializers.BookSerializer

