import io
class File(io.RawIOBase):

Defining a File-Like Object
class File:

    def __init__(self, file_name):
        self.file_name = file_name
        self._file = None

    def __enter__(self):
        self._file = open(self.file_name, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    def write(self, line):
        self._file.write(line + '\n')

    # Add read() and other methods here

file = File('sample.txt')
file.write('This is the first line')
file.write('This is the second line')
Making use of our custom object with a context manager
with File('sample.txt') as file:
    file.write('This is the first line')
    file.write('This is the second line')

with File('sample.txt') as file:
    print(file.readlines())
"""
import os

class File:

    def __init__(self, filename
