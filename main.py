from stats import number_of_characters, number_of_words, sorted_dict


def get_book_text(filename: str):
    with open(filename) as f:
        text = f.read()
        return text


def main():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    num_characters = number_of_characters(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted = sorted_dict(num_characters)
    for k in sorted:
        if not k["char"].isalpha():
            continue
        else:
            print(f"{k['char']}: {k['num']}")
    print("============= END ===============")


main()
