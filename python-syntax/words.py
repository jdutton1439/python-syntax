def print_upper_words1(words):
    """
        Prints each word from the words list in upper case
    """
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """
        Prints each word from words list that
        starts with 'e' or 'E' in upper case
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """
        Prints each word from the words list that
        starts with the values in must_start_with
        in upper case
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words1(["hello","hey","yo","goodbye","yes"])
print_upper_words2(["hello","eagle","yo","goodbye","yes","Ethereal"])
print_upper_words3(["hello","eagle","yo","goodbye","yes","Ethereal"], {"e","y"})