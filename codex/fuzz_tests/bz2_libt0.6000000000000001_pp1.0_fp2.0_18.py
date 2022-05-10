import bz2
bz2.decompress(d)

import os
os.listdir()

import glob
glob.glob('*.txt')

import string
string.punctuation

##
## Part 1
##

def word_count(filename):
    """Counts the approximate number of words in a file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    word_count(filename)

##
## Part 2
##

def count_the_
