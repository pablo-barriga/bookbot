import sys
from stats import word_count, character_count, sort_on

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read() #contains the file contents as a string

def list_conversion(char):
    sorted_key = []
    for key in char:
        sorted_key.append({"char": key,"num": char[key] })
    return sorted_key

def main():
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book = get_book_text(path_to_file)
    count = word_count(book)
    char_count = character_count(book)
    formatted_list = list_conversion(char_count)
    formatted_list.sort(reverse = True, key=sort_on)

    #formatting....
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ${path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in formatted_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()