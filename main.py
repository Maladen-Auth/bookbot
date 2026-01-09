from stats import word_count, char_count, char_list_expand
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text ():
    """
    book_path = input("Enter book file path: ")
    with open(book_path) as book_content:
        book = book_content.read()
    print(book)
    return
    """

    with open(sys.argv[1]) as book_content:
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
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_book_text()
    word_count(current_book)
    print("--------- Character Count -------")
    char_count(current_book)
    char_list_expand(char_list)
    print("============= END ===============")
    return


main()
    