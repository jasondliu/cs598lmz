import bz2
bz2.BZ2File('test.bz2','w')

# bzip2 compression
import bz2
bz2.compress(b'hello world!')

# gzip compression
import gzip
gzip.compress(b'hello world!')

# gzip file with filename
import gzip
gzip.open('test.gz','wt')

# gzip compression
import gzip
gzip.compress(b'hello world!')

# lzma compression
import lzma
lzma.LZMAFile('test.xz','w')

# lzma compression
import lzma
lzma.compress(b'hello world!')

# lzma compression
import lzma
lzma.compress(b'hello world!',lzma.FORMAT_XZ)

# lzma compression
import lzma
lzma.compress(b'hello world!',lzma.FORMAT_ALONE)

# lzma compression
import lzma
lzma.comp
