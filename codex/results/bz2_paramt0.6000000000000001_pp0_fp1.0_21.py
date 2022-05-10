from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('../data/enwik9.bz2').read())

# result: Error
# Python 2.7.6 
# bz2.BZ2File('../data/enwik9.bz2').read()
# result: Error
</code>
I am using Python 2.7.6 (64 bit) on Windows 10.
Any help is much appreciated.


A:

The bz2 module is only meant for decompressing single bz2 files.  You can't just decompress the concatenation of the two files.
You could use the Python bz2 module to decompress the files one after the other, but that's probably not the most efficient solution.

