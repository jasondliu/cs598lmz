import lzma
lzma.open("test.txt.xz")

# xz
import lzma
lzma.open("test.txt.xz", mode='rt')

# xz (lowercase)
import lzma
lzma.open("test.txt.xz", mode='rt')

# xz (uppercase)
import lzma
lzma.open("test.txt.XZ", mode='rt')

# gz
import gzip
gzip.open("test.txt.gz")

# gz
import gzip
gzip.open("test.txt.gz", mode='rt')

# gz (lowercase)
import gzip
gzip.open("test.txt.gz", mode='rt')

# gz (uppercase)
import gzip
gzip.open("test.txt.GZ", mode='rt')

# bz2
import bz2
bz2.open("test.txt.bz2")

# bz2
import bz2
bz2.open("test
