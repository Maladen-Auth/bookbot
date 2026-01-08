from stats import word_count, char_count, char_list_expand

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
    
    return book

current_book = get_book_text()
char_list = char_count(current_book)

"""
def word_count(book):
    words = book.split()
    print(f"Found {len(words)} total words")
    return
"""

def main():
    get_book_text()
    word_count(current_book)
    char_count(current_book)
    char_list_expand(char_list)
    return


main()
    