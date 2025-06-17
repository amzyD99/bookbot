'''
Bookboot
current functionality: none
only thing that exists here is a function that returns content of the book
'''
from stats import count_words, count_chars, sort_letters

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
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_count = count_chars(book_txt)
    sorted_count = sort_letters(char_count)
      
    for i in sorted_count:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
        
    print("============= END ===============")


main()