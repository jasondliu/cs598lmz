import bz2
bz2.BZ2File(filename)

# Open a gzip-compressed file in binary mode
import gzip
gzip.open(filename, mode='rb')

# Open a bz2-compressed file in text mode
import bz2
bz2.BZ2File(filename, mode='wt')

# Read from a gzip-compressed file
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# Write to a gzip-compressed file
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# Read from a bz2-compressed file
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# Write to a bz2-compressed file
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

#
