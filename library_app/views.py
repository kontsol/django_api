from django.shortcuts import render, get_object_or_404
from .models import Author, Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status



def author_list(request):
  authors = Author.objects.all()
  return render(request, 'author_list.html', {"authors": authors})

def book_list(request):
  books = Book.objects.all()
  return render(request, 'book_list.html', {"books": books})  

def homepage(request):
  return render(request, "base.html")



@api_view(['GET'])
def Book_API(request):

  books = Book.objects.all()
  serializer = BookSerializer(books, many=True)
  return Response(serializer.data)



@api_view(['GET'])
def Author_API(request):

  authors = Author.objects.all()
  serializer = AuthorSerializer(authors, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def addBook(request):

    author_name = request.data.get('author')
    first_name = author_name['first_name']
    last_name = author_name['last_name']

    try:
      author = Author.objects.get(first_name__iexact=first_name, last_name__iexact=last_name)
    except Author.DoesNotExist:
      return Response({"error": "Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    book_name = request.data.get('name')
    if Book.objects.filter(name=book_name, author=author).exists():
      return Response({"error": "This book already exists."}, status=status.HTTP_404_NOT_FOUND)

    # import pdb; pdb.set_trace()
    serializer = BookSerializer(data=request.data)
    # import pdb; pdb.set_trace()
    if serializer.is_valid():
      serializer.save()
    
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addAuthor(request):

  first_name = request.data.get('first_name')
  last_name = request.data.get('last_name')


  if not first_name or not last_name:
    return Response({"error": "Both first name and last name are required."}, status=status.HTTP_400_BAD_REQUEST)

  # if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
  #   return Response({"error": "This author already exists."}, status=400)

  serializer = AuthorSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)


@api_view(['GET'])
def search_author_books(request):
  first_name = request.data.get('first_name')
  last_name = request.data.get('last_name')

  if not first_name or not last_name:
    return Response({"error": "Please provide both first_name and last_name"}, status=status.HTTP_400_BAD_REQUEST)

  try:
    author = Author.objects.get(first_name__iexact=first_name, last_name__iexact=last_name)
  except:
    return Response({"error": "Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
  
  books = Book.objects.filter(author=author)
  serializer = BookSerializer(books, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_book(request, pk):

  try:
    book = Book.objects.get(pk=pk)
  except Book.DoesNotExist:
    return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

  book_name = request.data.get("name")
  book_public_date = request.data.get("publication_date")
  book_author = request.data.get("author")


  if book_name:
    book.name = book_name

  if book_public_date:
    book.publication_date = book_public_date

  if book_author:
    first_name = book_author.get("first_name")
    last_name = book_author.get("last_name")

    if first_name and last_name:
      try:
        author = Author.objects.get(first_name=first_name, last_name=last_name)

      except Author.DoesNotExist:
        book.author.first_name = first_name
        book.author.last_name = last_name
        book.author.save()
      else:
        book.author = author

  book.save()
  # import pdb; pdb.set_trace()



  serializer = BookSerializer(book)
  return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def single_book(request, pk):
  print(f'primary key {pk}')
  try:
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)
  except Book.DoesNotExist:
    return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
  
@api_view(['GET'])
def single_author(request, pk):
  try:
    author = Author.objects.get(pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)
  except Author.DoesNotExist:
    return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
  

@api_view(['DELETE'])
def delete_book(request, pk):
  try:
    book = Book.objects.get(pk=pk)
    book.delete()
    return Response({'message': 'Book deleted'}, status=status.HTTP_200_OK)
  except Book.DoesNotExist:
    return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_author(request, pk):
  try:
    author = Author.objects.get(pk=pk)
    author.delete()
    return Response({'message': 'Author deleted'}, status=status.HTTP_200_OK)
  except Author.DoesNotExist:
    return Response({'message': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)




