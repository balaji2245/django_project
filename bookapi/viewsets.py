from rest_framework import viewsets
from . import models
from . import serializers

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    
#     dict1 = {"status_code": 200, "status": "success", "data": queryset}
#     print("++++++++++++++====")
#     queryset = dict1
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{{{{}{}{}{[][][[][][]]")
    print(models.Book.objects.get(id=1))
    serializer_class = serializers.BookSerializer

