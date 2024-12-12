'''
New Information will include:
• Data Validation, Exception Handling, Status Codes, Swagger
Configuration, Python Request Object

use Pydantics
'''

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from models import BookRequest
from starlette import status

app = FastAPI()

'''
create a class Book
'''


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


# ----------------models


# ---initial BOOKS
BOOKS = [
    Book(1, "My Lady Love", "Taylor Ann Bunker",
         "When twenty year old, professional witch hunter, Victor Steep is summoned to handle a case", 4),
    Book(2, "Don't Close Your Eyes", "Lynessa James (Goodreads Author)", "An enemies to lovers series begins.", 4),
    Book(3, "Avenue of Death", "Akash Bansal",
         "University of Stanmore’s grand and gothic structure was intimidating, and so were its uniquely and incomprehensibly built underground territory.",
         5),
    Book(4, "Gatsby's Smile", "Morana Blue", "Gatsby's Smile is a psychological thriller/murder mystery.", 4),
    Book(5, "Just Pretending", "Dana Burkey",
         "Everything in Cam’s life is finally going right. Despite many of her best friend being out of town for the summer, she is ready to have some fun.",
         4)
]



@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.post("/books/create_book", status_code=status.HTTP_201_CREATED)
async def create_new_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))
    return {"message": "create successful"}


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book


@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def read_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    # return {"message": "book not found"}
    raise HTTPException(status_code=404, detail= "item not found" )

@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == rating:
            books_to_return.append(book)
    return books_to_return


@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
