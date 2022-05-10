import codecs
codecs.register_error('strict', codecs.ignore_errors)

import struct
import copy
import random
import itertools

def unescape(s):
    """
    Unescape \\\" to \"
    """
    res = s.replace(r'\\"', '"')
    res = res.replace(r'\\', '\\')
    return res

def escape(s):
    """
    Escape \" to \\\"
    """
    res = s.replace('\\', r'\\')
    res = res.replace('"', r'\"')
    return res

def word_tokenize(sentence, lower=True):
    try:
        sentence = sentence.replace(u"\u2019", "'") # special apostrophe
        sentence = sentence.replace(u"\u2018", "'") # special apostrophe
        sentence = sentence.replace(u"\u201c", '"') # left double quote
        sentence = sentence.replace(u"\u201d", '"') # right double quote
        sentence = sentence.replace(u"\u2013", '-
