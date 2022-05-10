import mmap
import re
import sys
import os
from collections import Counter

# The following code is used to deal with UTF-8 encoding errors in Windows
reload(sys)
sys.setdefaultencoding('utf8')

# This function takes a filename and returns the entire
# contents of the file as a string
def get_data(filename):
    f = open(filename)
    data = f.read()
    f.close()
    return data

# This function takes a string containing the contents of a text file
# and returns a list of all the words in the file
def get_words_from_string(string):
    word_list = re.findall('\w+', string.lower())
    return word_list

# This function takes a list of words and returns a dictionary
# associating words with frequencies of occurrence
def get_freqs(word_list):
    freq_mapping = Counter(word_list)
    return freq_mapping

# This function takes a dictionary mapping words to frequencies
# and returns a list of pairs where the entries are sorted from
# highest to
