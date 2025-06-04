def get_number_words(book_text):
    return len(book_text.split())

def get_character_count(book_text):
    characters = {}

    for char in book_text:
        char_l = char.lower()
        if char_l in characters:
            characters[char_l] += 1
        else:
            characters[char_l] = 1
    
    return characters

def sort_on(dict):
    return dict["num"]

def get_sorted_dictionary(character_list):
    sorted_list = []

    for char in character_list:
        sorted_list.append({"char": char, "num": character_list[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list