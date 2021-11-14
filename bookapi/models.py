from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    authors = models.CharField(max_length=100)      ####1
    number_of_pages = models.CharField(max_length=10)           ####2
    publisher = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    

#CRUD

#Create (POST)


#Read (GET)


#Update (PUT)


#Delete (DELETE)

