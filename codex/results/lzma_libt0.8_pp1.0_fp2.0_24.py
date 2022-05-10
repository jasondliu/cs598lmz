import lzma
lzma.decompress()
'''

import gzip
import tarfile
tarfile.open("tarfile.tar.gz")
f = gzip.open("gzip_compressed.txt.gz", "rb")

f.read()
f.close()
