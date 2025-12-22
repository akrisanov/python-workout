def pig_latin(word: str) -> str:
    if not word:
        return word

    pig_word = f"{word}way" if word[0].lower() in "aeiou" else f"{word[1:]}{word[0]}ay"

    is_capitalized = word[:1].isupper() and word[1:].islower()
    if is_capitalized:
        return pig_word[:1].upper() + pig_word[1:].lower()

    return pig_word


if __name__ == "__main__":
    print(pig_latin("air"))
    print(pig_latin("eat"))
    print(pig_latin("python"))
    print(pig_latin("computer"))
    print(pig_latin("Hello"))
