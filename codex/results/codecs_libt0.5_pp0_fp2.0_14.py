import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import sys

def main():
    # get the file name
    fname = sys.argv[1]
    # open the file
    f = open(fname, 'r')

    # how many words we've seen so far
    n = 0
    # how many words we've seen with a certain length
    n_k = {}
    # how many words we've seen with a certain length that have a certain last
    # letter
    n_kl = {}

    # read the file line by line
    for line in f:
        # split the line into words
        words = line.split()
        # for each word
        for word in words:
            # count the word
            n += 1
            # get the length of the word
            k = len(word)
            # count the word with this length
            if k in n_k:
                n_k[k] += 1
            else:
                n_k[k] = 1
           
