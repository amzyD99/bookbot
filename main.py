'''
Bookboot
current functionality: none
only thing that exists here is a function that returns content of the book
'''
from stats import count_words

def get_book_text(book_path):
    with open(book_path) as f:
        book_content = f.read()
    return book_content


def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_txt = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_txt)
    print(f"{word_count} words found in the document")
    
main()