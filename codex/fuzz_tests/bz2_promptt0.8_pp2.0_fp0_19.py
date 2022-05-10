import bz2
# Test BZ2Decompressor --- best used from the command line
# f = bz2.BZ2Decompressor()
# f.decompress(data)

import random

def random_string(length=128, alphabet="abcdefghijklmnopqrstuvwxyz"
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        "0123456789"):
    """Generate a random Unicode string of a given length (in characters)

    :param int length: The desired length of the random string
    :param str alphabet: The characters to use in generating the string

    :return: A random string of the given length, composed of the given alphabet
    :rtype: str
    """

    source = [c for c in alphabet]
    strlen = len(alphabet)

    return ''.join([source[random.randint(0, strlen-1)]
                    for _ in range(length)])

def random_ascii_string(length=128, alphabet="abcdefghijklmnopqrstuvwxyz"
                        "ABCDEF
