import bz2
bz2.BZ2File('compressed.bz2').read()

# compressing with gzip
import gzip
import shutil
with gzip.open('compressed.gz', 'wt') as f:
    f.write("Line 1")
    f.write("Line 2")
    f.write("Line 3")

# the 'w' flag means write mode
# the 't' flag means text mode (could also be 'b' for binary)

# you can combine both 'w't and 'b' like: 'wb'

# note: a gzip file doesn't allow multiple streams/members like a zip file.

# gzip also has a compress level argument.
import gzip
with gzip.open('compressed.gz', 'wt', compresslevel=5) as f:
    f.write("Line 1")
    f.write("Line 2")
    f.write("Line 3")

# note: after a gzip file has been open in write mode, you cannot open it again in read mode or append mode.

# decompressing with gzip
import gzip

