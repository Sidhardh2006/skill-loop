import requests
import webbrowser

def get_books(query):
    # Define the API URL
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

    # Make the GET request to the API
    response = requests.get(url)

    # If the request is successful, process the data
    if response.status_code == 200:
        books = response.json()['items']
        return books
    else:
        return None

def display_books(books):
    # Check if we have books to display
    if books:
        print(f"Top {len(books)} books based on your search:\n")
        for index, book in enumerate(books, 1):
            title = book['volumeInfo'].get('title', 'No title available')
            authors = ', '.join(book['volumeInfo'].get('authors', ['No authors available']))
            description = book['volumeInfo'].get('description', 'No description available')
            print(f"{index}. Title: {title}")
            print(f"   Authors: {authors}")
            print(f"   Description: {description}\n")
    else:
        print("No books found for your search query.")

def main():
    search_query = input("Enter a book title or author to search: ")
    webbrowser.open("https://www.google.com/search?udm=36&q="+search_query)
    books = get_books(search_query)
    display_books(books)

if _name_ == "_main_":
    main()
