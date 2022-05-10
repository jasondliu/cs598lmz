import mmap
import math
from ProgressBar import ProgressBar



def isInt(i):
    try:
        int(i)
    except ValueError:
        return False
    return True


def map_file(filename):
    f = open(filename, "r+")
    s = mmap.mmap(f.fileno(), 0)
    return s


def findInts(s):
    return [i for i in re.findall(r"[\+-]?\d+\.?\d*", s)]


def find_complete_words(o_string, test_string):
    allowables = ["(", ")", "*", "|"]
    output = []

    while len(o_string) > 0:

        if o_string[0] in allowables:
            output.append(o_string[0])
            o_string = o_string[1:]
            continue

        word = o_string[0]
        test_string.append(word)
        o_string = o_string[1:]

        while word not in allowables
