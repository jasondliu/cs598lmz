import ctypes
ctypes.cast(pointer, ctypes.py_object).value


def count_em(arr):
    """
    Counts the different letters in an array
    :param arr: array of characters
    :return: dictionary of counts
    """
    alphabet = string.ascii_lowercase
    counts = {}
    for x in alphabet:
        counts[x] = 0
    for x in arr:
        counts[x] += 1
    return counts


def is_anagram(a, b):
    """
    Checks if a and b are anagrams
    :param a: word a
    :param b: word b
    :return: True if anagrams, false otherwise
    """
    if len(a) != len(b):
        return False
    counts_a = count_em(a)
    counts_b = count_em(b)
    for x in counts_a:
        if counts_a[x] != counts_b[x]:
            return False
    return True


def anagrams(s, words):
    """
    Finds the anagram
