import bz2
bz2.compress(b"hello world")

bz2.decompress(b"BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")

with bz2.open("test.bz2", "wt") as fout:
    fout.write("hello world")

with bz2.open("test.bz2", "rt") as fin:
    print(fin.read())

import gzip
with gzip.open("test.gz", "wt") as fout:
    fout.write("hello world")

with gzip.open("test.gz", "rt") as fin:
    print(fin.read())

with gzip.open("test.gz", "wt") as fout:
    fout.write("hello world")

with gzip.open("test.gz", "rt") as fin:
   
