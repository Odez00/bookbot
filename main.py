from stats import number_of_characters, number_of_words


def get_book_text(filename: str):
    with open(filename) as f:
        text = f.read()
        return text


def main():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    num_characters = number_of_characters(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    print(num_characters)


main()
