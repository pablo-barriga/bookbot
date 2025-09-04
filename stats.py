def word_count(book):
    words = book.split()
    return len(words)

def character_count(book):
    char_count = {}
    for character in book:
        character = character.lower()
        if character not in char_count:
            char_count[character] = 0
        char_count[character] +=  1
    
    return char_count


def sort_on(char):
    return char["num"]

    