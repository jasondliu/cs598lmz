import bz2
bz2.BZ2Compressor()

import bz2

help(bz2.BZ2Compressor)

import bz2
help(bz2.BZ2Decompressor)

import bz2

help(bz2.BZ2Decompressor.read)

import bz2
help(bz2.BZ2File)

import bz2

help(bz2.BZ2File.read)

import bz2
print(bz2.BZ2File.read.__doc__)

import bz2

f = bz2.open("text.bz2", mode="wt")

f.write("The quick brown fox jumps over the lazy dog.")

f.close()

import bz2

f = bz2.open("text.bz2", mode="wt")

f.write("The quick brown fox jumps over the lazy dog.")

f.close()

import bz2

f = bz2.open("text.bz2", mode="rt")
