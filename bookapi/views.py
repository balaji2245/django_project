from django.shortcuts import render

# Create your views here.

from .serializers import BookSerializer


class BookList(APIView):
  def get(self, request):
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


