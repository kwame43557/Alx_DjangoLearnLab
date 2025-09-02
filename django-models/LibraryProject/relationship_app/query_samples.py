from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    author = Author.objects.get(name="Chinua Achebe")
    books_by_author = Book.objects.filter(author=author)
    print("Books by", author.name, ":", [book.title for book in books_by_author])

    # 2. List all books in a library
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print("Books in", library.name, ":", [book.title for book in books_in_library])

    # 3. Retrieve the librarian for a library
    librarian = library.librarian  # thanks to related_name="librarian"
    print("Librarian of", library.name, ":", librarian.name)