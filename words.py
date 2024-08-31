word_list = ["hello", "hey", "goodbye", "yo", "yes", "every", "Edge"]


def print_upper_words(word_list, must_start_with):
    """Print all words in the list in upper case that start with the letters passed in."""

    for word in word_list:
        for letter in must_start_with:
            if letter.upper() == word[0].upper():
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
