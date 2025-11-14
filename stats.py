def number_of_words(text: str):
    words = text.split()
    return len(words)


def number_of_characters(text: str):
    characters = {}
    for character in text:
        if character.lower() in characters:
            characters[character.lower()] += 1
        else:
            characters[character.lower()] = 1
    return characters


def sorted_dict(words: dict):
    def sort_on(items):
        return items["num"]

    sorted = []
    for char in words:
        sorted.append({"char": char, "num": words[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
