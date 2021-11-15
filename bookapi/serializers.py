from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        dict = {"status_code": 200, "status": "success", "data": fields}
        fields = dict
