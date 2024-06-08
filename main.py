def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars = char_count(text)
    char_sorted_list = char_dict_to_sorted_list(chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    
    print("--- End report ---")
    
def word_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(num_char_dict):
    sorted_list = []
    for char in num_char_dict:
        sorted_list.append({"char": char, "num": num_char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return(sorted_list)

def char_count(text):
    text_lowercase = text.lower()
    char_dict = {}
    for char in text_lowercase:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return(char_dict)

def get_book_text(path):    
    with open(path) as f:
        return f.read()

main()