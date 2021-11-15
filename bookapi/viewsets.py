from rest_framework import viewsets
from . import models
from . import serializers

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    
#     dict1 = {"status_code": 200, "status": "success", "data": queryset}
#     print("++++++++++++++====")
#     queryset = dict1
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{{{{}{}{}{[][][[][][]]")
    temp = models.Book.objects.get(id=1)
    print(temp.name)
    print(len(queryset))
    temp1 = []
    temp1.append(queryset[0])
    dict1 = {"status_code": 200, "status": "success", "data":temp1}
    
    print(temp1)
    print(dict1)
    
    serializer_class = serializers.BookSerializer

