books = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
    {"title": "The Giver", "author": "Lois Lowry"},
    {"title": "Charlotte's Web", "author": "E.B. White"},
]


def find_books(books, query):
    """Return books whose titles contain query, ignoring capitalization."""
    matches = []

    # TODO: Use a loop to add matching books to matches.

    return matches


def sort_books_by_title(books):
    """Return a new list sorted by title using insertion sort."""
    sorted_books = books.copy()

    # TODO: Implement insertion sort without changing books.

    return sorted_books


if __name__ == "__main__":
    search_results = find_books(books, "the")
    sorted_results = sort_books_by_title(books)

    print("Search results:")
    for book in search_results:
        print(f"{book['title']} by {book['author']}")

    print("\nBooks sorted by title:")
    for book in sorted_results:
        print(f"{book['title']} by {book['author']}")