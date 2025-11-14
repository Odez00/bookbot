import sys

from stats import number_of_characters, number_of_words, sorted_dict


def get_book_text(filename: str):
    with open(filename) as f:
        text = f.read()
        return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = number_of_words(get_book_text(sys.argv[1]))
    num_characters = number_of_characters(get_book_text(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
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
