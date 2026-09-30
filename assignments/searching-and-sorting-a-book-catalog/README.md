# 📘 Assignment: Searching and Sorting a Book Catalog

## 🎯 Objective

Practice working with lists and dictionaries by implementing a linear search and an insertion sort for a small book catalog.

## 📝 Tasks

### 🛠️ Search the Catalog

#### Description
Complete `find_books(books, query)` so students can search a catalog by part of a book title. The search should ignore capitalization and return every matching book.

#### Requirements
Completed program should:

- Store each book as a dictionary with `title` and `author` keys
- Search titles with a loop and a case-insensitive comparison
- Return a list containing all matching books, or an empty list when there are no matches
- Leave the original catalog unchanged

Example:

```text
Search: the
Matches: The Hobbit by J.R.R. Tolkien, The Giver by Lois Lowry
```

### 🛠️ Sort the Catalog

#### Description
Complete `sort_books_by_title(books)` using insertion sort. Return a new list of books in ascending title order, without changing the original catalog.

#### Requirements
Completed program should:

- Compare titles without regard to capitalization
- Implement insertion sort with loops rather than calling `sort()` or `sorted()`
- Return a new sorted list and preserve the input list's order
- Demonstrate both the search and sorted results using the sample catalog