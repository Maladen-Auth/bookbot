

def get_book_text ():
    """
    book_path = input("Enter book file path: ")
    with open(book_path) as book_content:
        book = book_content.read()
    print(book)
    return
    """

    with open("books/frankenstein.txt") as book_content:
        book = book_content.read()
    # print(book)
    
    words = book.split()
    print(f"Found {len(words)} total words")
    
    
    return

"""
def word_count():
    words = book.split
    print(len(words))
    return
"""

def main():
    get_book_text()
    # word_count()
    return


main()
    