from django.db import models
 
# Create your models here.
class Article(models.Model):                    # you will create a table called Article
   title = models.CharField(max_length=100)    # ids are created automatically so you don't have to create an id
   description = models.TextField()
 
   def __str__(self):
       return self.title