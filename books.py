from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Book One", "author": "Author One", "category": "science"},
    {"title": "Book Two", "author": "Author Two", "category": "math"},
    {"title": "Book Three", "author": "Author Three", "category": "history"},
    {"title": "Book Four", "author": "Author Four", "category": "space"},
    {"title": "Book Five", "author": "Author Five", "category": "science"},
    {"title": "Book Six", "author": "Author One", "category": "history"}
]


@app.get("/api-endpoint")
async def greeting():
    return {"message": "Welcome to Fastapi"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return None

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/by_author/")
async def read_books_by_author_path(author:str):
    books_to_return= []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_new_book(new_book = Body()):
    BOOKS.append(new_book)
    return {"message": "create successful"}


@app.put("/books/update_book")
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book
            return {"message": "update successful"}


@app.delete("/book/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {"message": "The book has deleted"}

    else:
        return {"message": "Not book found"}

