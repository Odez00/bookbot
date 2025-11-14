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
