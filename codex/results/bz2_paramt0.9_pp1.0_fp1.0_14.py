from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('train.csv.bz2', 'rb').read())
</code>
I am using python 2.6
The error is "Error -3 while decompressing: invalid stored block lengths".


A:

Use this module:
https://pypi.python.org/pypi/bz2file

