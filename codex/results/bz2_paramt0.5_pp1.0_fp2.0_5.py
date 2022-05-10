from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('test.bz2', 'rb').read())

# bz2.open(filename[, mode[, compresslevel]])
#   Open a bz2 file.
#
#   The mode can be 'r' or 'w', for reading (default) or writing.
#
#   The file will be closed when it is garbage collected.
#
#   compresslevel is an integer from 1 to 9 controlling the level of
#   compression; 1 is fastest and produces the least compression, and 9 is
#   slowest and produces the most compression. The default is 9.
#
#   Add a 'U' to mode to open the file for input with universal newline
#   support. Any line ending in the input file will be seen as a '\n' in
#   Python. Also, a file so opened gains the attribute 'newlines'; the value
#   for this attribute is one of None (no newline read yet), '\r', '\n',
#   '\r\n' or a tuple containing all the newline types seen. Universal
#   newlines are available only
