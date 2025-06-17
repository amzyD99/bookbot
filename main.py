'''
Bookboot
current functionality: none
only thing that exists here is a function that returns content of the book
'''
from stats import count_words, count_chars

def get_book_text(book_path):
    with open(book_path) as f:
        book_content = f.read()
    return book_content


def main():
    print("============ BOOKBOT ============")
    book_path = "./books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}")
    book_txt = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count = count_words(book_txt)
    print(f"{word_count} words found in the document")

    print("--------- Character Count -------")
    char_count, chars = count_chars(book_txt)

    for char in chars:
        if char.isalpha():
            print(f"{char}: {char_count[char]}\n")
    print("============= END ===============")


main()