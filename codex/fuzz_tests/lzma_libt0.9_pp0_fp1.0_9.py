import lzma
lzma.open("file.txt")
#you can use lzma.open() or zlib.compress() like open() function

import zlib
zlib.open("file.txt")

"""

"""
Compressing Data in python
"""
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s) # here we compress the file
print(len(t)) #print length of compressed file

print(zlib.decompress(t)) #we get back our string

print(zlib.crc32(s)) #we get the crc32 checksum of the string

"""

"""
"""
compression
"""

import bz2
b = bz2.compress(s)
print(len(b))
print(bz2.decompress(b))

"""
"""
The lzma library provides additional compression modes, which require including a mode value in the call with the compress() method:
lzma.LZMA_MODE_FASTest

