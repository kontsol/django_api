from django.db import models

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)

  def __str__(self):
    return self.first_name
  

class Book(models.Model):
  name = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  date_added = models.DateField(auto_now_add=True)
  publication_date = models.DateField()


  def __str__(self):
    return self.name