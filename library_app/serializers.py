from rest_framework import serializers
from library_app.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = "__all__"

class BookSerializer(serializers.ModelSerializer):

  author = AuthorSerializer()

  class Meta:
    model = Book
    fields = ["id", 'name', 'date_added', 'publication_date', 'author']


  def create(self, validated_data):
      author_data = validated_data.pop('author')
      author_instance, _ = Author.objects.get_or_create(**author_data)
      book = Book.objects.create(author=author_instance, **validated_data)
      return book
