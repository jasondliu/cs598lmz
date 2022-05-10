import lzma
lzma.open('test.txt.xz').read()

# gzip
import gzip
gzip.open('test.txt.gz').read()

# bz2
import bz2
bz2.open('test.txt.bz2').read()
