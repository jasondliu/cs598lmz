import io
# Test io.RawIOBase
# See http://docs.python.org/3.3/library/io.html#io.RawIOBase
# for more information about the methods and attributes.

# Write a small program that takes a path to a file and prints the
# contents of that file to the terminal. If no path is passed, the
# program should quit.

# This example uses the assert method to verify that the file is
# opened, but assert should not be used in production code.

# Assume that a file has the following contents:
#   I love cats.
#   I love dogs.
#   I love pickles.
#   I love unicorns.

# The program should print the following to the terminal:
#   I love cats.
#   I love dogs.
#   I love pickles.
#   I love unicorns.

import sys

class RawIOHandler(io.RawIOBase):
    def __init__(self, file_path):
        self.file = open(file_path)

    def read(self):
        return self.file.read()

