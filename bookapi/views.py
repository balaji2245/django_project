from django.shortcuts import render

# Create your views here.

from .serializers import BookSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


# class BookList(APIView):

@api_view()
@permission_classes([AllowAny])
def get(request):
  print("requested {{{{{{{{{{{{{{{{{{")
    
  my_books = Book.objects.all()
  serializer = BookSerializer(my_books, many= True)
    
  my_dict = {
    "status_code":200,
    "stats": "success",
    "data": serializer.data,
  }
    
  res = Response(my_dict)
    
  return res

def post(self):
 pass


