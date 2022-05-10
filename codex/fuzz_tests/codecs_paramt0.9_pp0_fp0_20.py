import codecs
codecs.register_error("strict", codecs.ignore_errors)
import unicodedata
import sys
import os

sys.path.append("..")
from normalization.transformations import *

verbose = False

# This is for compatibility with py2exe
try:
    from functools import reduce
except:
    pass

def parse_ngram_line(line):
    """input line is a string indicating an ngram w1 w2 ... wn \t count
       output is a dictionary of (n-1)-grams mapping to a dictionary of vocab words
       mapping to count
    """
    line = unicodedata.normalize("NFKD", unicode(line)).encode("ascii", "strict")
    line = line.rstrip()
    [ngram, count] = re.split(r"\t", line)
    [w0, w1, w2, w3, w4, w5, w6, w7] = re.split(r"\s+", ngram)
    w = [w0, w1, w2, w3
