import bz2
bz2c = bz2.BZ2Compressor()
bz2d = bz2.BZ2Decompressor()
#DECOMPRESS
with open("/mnt/store/20101130/20101130-2301.txt.bz2", "rb") as f:
    text = bz2dec.decompress(f.read())
#TRAIN
from string import punctuation

import re
import collections

import random
from itertools import cycle



def preprocess(text):
    text = re.sub("<[^<]+?>", "", text)
    for p in punctuation:
        text = text.replace(p, " " + p + " ")
    text = text.lower()
    return text.split()

def train_markov(text, n=1):
    model = collections.defaultdict(collections.Counter)
    for i in range(len(text) - n):
        ngram = text[i: i + n]
        next_word = text[i + n]
        model[t
