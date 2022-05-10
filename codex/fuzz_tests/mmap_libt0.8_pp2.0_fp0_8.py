import mmap

def get_words(path):
    """
    Gets the words from a dictionary path.
    """
    words = []
    with open(path, "r+b") as f:
        m = mmap.mmap(f.fileno(), 0)
        for line in iter(m.readline, ""):
            word = line.rstrip()
            words.append(line.rstrip())
    return words

def isWord(word):
    """
    Checks if a word is in the dictionary.
    """
    words = get_words("/usr/share/dict/words")
    return word in words

def get_one_letter_words():
    """
    Gets all the one letter words in the dictionary.
    """
    words = get_words("/usr/share/dict/words")
    one_letter_words = []
    for w in words:
        if len(w) == 1:
            one_letter_words.append(w)
    return one_letter_words

def get_two_letter_words():
    """

