import sys
from stats import get_number_words
from stats import get_character_count
from stats import get_sorted_dictionary

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_number_words(book_text)
    character_count = get_character_count(book_text)
    sorted_list = get_sorted_dictionary(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()