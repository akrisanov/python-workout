import string


def pig_latin(word: str) -> str:
    if not word:
        return word

    is_capitalized = word[0].isupper() and word[1:].islower()
    punctuation = ""

    if word[-1] in string.punctuation:
        punctuation = word[-1]
        word = word[:-1]

    if word[0].lower() in "aeiou":
        pig_word = f"{word}way"
    else:
        pig_word = f"{word[1:]}{word[0]}ay"

    if is_capitalized:
        pig_word = pig_word[0].upper() + pig_word[1:].lower()

    return pig_word + punctuation


if __name__ == "__main__":
    print(pig_latin("air"))
    print(pig_latin("eat"))
    print(pig_latin("python"))
    print(pig_latin("Python?"))
    print(pig_latin("computer."))
    print(pig_latin("Hello!"))
