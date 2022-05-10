import mmap
import sys
import os
import random

from collections import defaultdict
from operator import itemgetter
from math import log

class LanguageModel:
    def __init__(self, order, filename=None, lm=None):
        self.order = order
        self.lm = lm or defaultdict(lambda: defaultdict(int))
        self.vocab = set()

        if filename:
            self.read_file(filename)

    def read_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                count, *word = line.split()
                self.lm[tuple(word[:-1])][word[-1]] = int(count)
                self.vocab.add(word[-1])
        self.vocab.add('<UNK>')

    def write_file(self, filename):
        with open(filename, 'w') as f:
            for word, next_words in self.lm.items():
                for next_word, count in next_words.items
