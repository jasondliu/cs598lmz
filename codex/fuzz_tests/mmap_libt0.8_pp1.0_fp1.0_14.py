import mmap
import re
import sys

def main():
    file_name = 'rl.txt'

    with open(file_name, 'r+b') as file_handle:
        # mmap the file, size 0 means whole file
        mm = mmap.mmap(file_handle.fileno(), 0)

        # read content via standard file methods
        print(mm.readline())  # prints "Hello Python!\n"
        print(mm.readline())
        mm.seek(0)  # rewind
        line = mm.readline()   # Read the entire file.
        print(line)

        # read content via slice notation
        mm.seek(0)
        data = mm.read(2)
        print(data)
        data = mm.read(2)
        print(data)
        mm.seek(0)
        # Search start of file (index 0), end of file (index mm.size()),
        # using a regular expression.
        print(mm.find(b'\n', 1))
        print(mm.find(b'\
