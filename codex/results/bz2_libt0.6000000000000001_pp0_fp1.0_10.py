import bz2
bz2.BZ2File.read = lambda self, size: self.readline()

import sys
import re

class Entry:
    def __init__(self, line):
        self.line = line
        self.re_remove = re.compile(r'(https?:\/\/|www\.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
        self.re_remove_apostrophe = re.compile(r'\'s')
        self.re_remove_punctuation = re.compile(r'[^a-zA-Z0-9 ]')
        self.re_remove_space = re.compile(r'\s+')
        self.re_remove_digit = re.compile(r'\d+')
        self.re_remove_short = re.compile(r'\b\w{1,2
