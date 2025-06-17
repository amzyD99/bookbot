def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):

    chars = {}
    letters = []
    text_lowercase = text.lower()

    for char in text_lowercase:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] =1

    for char in chars:
        letters.append({"char": char, "num": chars[char]})
    
    return letters

def sort_letters(letters):
    letters.sort(reverse=True, key=sort_on)
    return letters

    
