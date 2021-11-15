from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        print(model, "++++==+++")
        fields = '__all__'
        print(fields[0], "------000")
        
#         dict = {"status_code": 200, "status": "success", "data": fields}
#         fields = dict

        
