def is_isogram(string):
    word = string.lower()
    phrase = []

    for letter in word:
        if letter.isalpha():
            if letter in phrase:
                return False
            phrase.append(letter)
    return True