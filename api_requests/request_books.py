import requests


def get_all_books(book_type="",limit=""):
    return requests.get(f"https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}")


# def get_all_books_parameters(book_type,limit):
#     return requests.get(f"https://simple-books-api.glitch.me/books?type={book_type}&limit={limit}")

def get_book(book_id):
    return requests.get(f"https://simple-books-api.glitch.me/books/{book_id}")

# print(get_all_books("non-fiction", 2).json())
# print(get_all_books().json())
# print(get_book(3).json())
