from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library   # <-- explicit import of Library

# -----------------------------
# Function-Based View
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# -----------------------------
# Class-Based View
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # <-- app name included
    context_object_name = "library"
