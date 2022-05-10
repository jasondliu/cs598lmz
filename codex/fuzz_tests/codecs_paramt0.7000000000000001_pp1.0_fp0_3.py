import codecs
codecs.register_error('strict', codecs.ignore_errors)

import numpy as np

def read_words(filename):
    """
    Read raw text into an array of words (sequences of characters)
    """
    with open(filename, 'r') as f:
        #utf-8 encoding should be used for the text files
        return f.read().decode('utf-8','strict').replace('\n',' ').split(' ')

def read_words_delim(filename, delim=None):
    """
    Read raw text into an array of words (sequences of characters)
    """
    with open(filename, 'r') as f:
        #utf-8 encoding should be used for the text files
        text = f.read().decode('utf-8','strict')
        if delim is None:
            return text.replace('\n',' ').replace('\t',' ').replace('-',' ').split(' ')
        else:
            return text.replace('\n',' ').replace('\t',' ').split(delim)

def read_
