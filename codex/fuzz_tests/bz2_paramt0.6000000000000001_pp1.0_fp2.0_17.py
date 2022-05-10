from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Reading from the File
# Python can read from files with the built-in open function.

# open takes the name of the file and the mode in which to open it.
# The mode can be either r for reading, w for writing or a for appending.

# The file is opened and a file object is returned.
# The file object can be used as an iterator over lines.

file = open('test.txt', 'r')
for line in file:
    print(line)

# It is also possible to read the entire file as a string,
# or to read it in chunks of a certain size.

file = open('test.txt', 'r')
file.read()

file = open('test.txt', 'r')
file.read(10)

# The readline method can be used to read a single line,
# and the readlines method can be used to read all lines into a list.

file = open('test.txt', 'r')
file.readline()

file = open('test.txt', '
