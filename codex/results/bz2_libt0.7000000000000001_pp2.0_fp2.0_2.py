import bz2
bz2.BZ2Compressor().compress(bz2.BZ2Compressor().compress(bz2.BZ2Compressor().compress(b'Hello, world!')))

def bzip2_recurse(b):
    return bz2.BZ2Compressor().compress(bz2.BZ2Compressor().compress(bz2.BZ2Compressor().compress(b)))
    
print(bzip2_recurse(b'Hello, world!'))

bzip2_recurse(b'Hello, world!').decode()

chr(1) + chr(2) + chr(3)

bzip2_recurse(b'Hello, world!').decode()[:10]

assert bzip2_recurse(b'Hello, world!').decode()[:10] == 'BZh91AY&S'

#!python

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts
