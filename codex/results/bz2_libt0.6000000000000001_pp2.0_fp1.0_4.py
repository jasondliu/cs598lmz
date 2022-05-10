import bz2
bz2.decompress(f.read())

# bz2.open()
# bz2.BZ2File()

# gzip
import gzip
f = gzip.open('file.gz', 'r')
f.read()
f.close()

# gzip.open()
# gzip.GzipFile()

# zlib
import zlib
zlib.decompress(f.read())
