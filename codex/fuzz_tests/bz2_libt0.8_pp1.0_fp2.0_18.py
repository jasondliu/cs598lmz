import bz2
bz2.decompress(test_text)

# This is not useful

# What is useful is knowing that the bz2 and gzip packages allow you to compress and decompress data in memory.
# This allows you to use standard Python tools to write compressed data to files using a file object.
# Reading compressed data from a file requires a different approach.

# Say you have a plain text file named 'test.py' that looks like this:
'''
print("This is a test")

print("This is another test")

print("This is yet another test")
'''

# you could open it, read in the contents and use compress to compress it before writing it to a file:

from bz2 import compress
test_text = open('test.py').read()
compressed = compress(test_text)
open('test.py.bz2', 'wb').write(compressed)

# the resulting file is a compressed bz2 archive called 'test.py.bz2' which contains the compressed data:

from bz2 import decompress
decompressed = decompress(open('
