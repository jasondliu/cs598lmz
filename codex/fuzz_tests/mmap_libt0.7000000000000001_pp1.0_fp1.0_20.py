import mmap
import math
import os
import sys
import functools

class TextModel:

    def __init__(self):
        """This constructor does nothing by default.  It's just a placeholder
        where you can put any global variables you want to use throughout the
        class.
        """
        self.model = {}
        self.numChars = 0
        self.numWords = 0

    def read_file(self, filename):
        """Read a text file, and train a model based on the contents.

        Arguments:
            filename (str): The name of the file to read.

        Returns:
            None
        """
        f = open(filename, "r")
        text = f.read()
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')
        text = text.replace('\t', ' ')
        text = text.replace('  ', ' ')
        text = text.replace('  ', ' ')
        text = text.replace('  ', ' ')
        text = text.replace
