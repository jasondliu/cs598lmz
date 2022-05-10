from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Writing to a File
# Opening a file with open() returns a file object, and is most commonly used with two arguments: open(filename, mode).

# Mode	Description
# "r"	This is the default mode. It Opens file for reading.
# "w"	This Mode Opens file for writing.
# If the file does not exist, it creates a new file.
# If the file exists it truncates the file.
# "x"	Creates a new file. If the file already exists, the operation fails.
# "a"	Open file in append mode.
# If the file does not exist, it creates a new file.
# "t"	This is the default mode. It opens in text mode.
# "b"	This opens in binary mode.
# "+"	This will open a file for reading and writing (updating)

# 'w' mode
f = open('workfile.txt', 'w')
f.write('This is a test\n')
f.write('Hello, world!\n')


