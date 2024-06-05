def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars = char_count(text)
    print(f"{chars} characters found in the document")
    
def get_book_text(path):    
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text_lowercase = text.lower()
    char_dict = {}
    for char in text_lowercase:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return(char_dict)
main()