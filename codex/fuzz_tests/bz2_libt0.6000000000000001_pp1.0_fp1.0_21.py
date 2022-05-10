import bz2
bz2_file = bz2.BZ2File("test.txt.bz2")
print(bz2_file.read())

import gzip
gzip_file = gzip.open("test.txt.gz", "rt")
print(gzip_file.read())
