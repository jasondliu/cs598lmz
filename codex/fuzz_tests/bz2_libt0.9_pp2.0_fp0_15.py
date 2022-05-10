import bz2
bz2_handler = bz2.BZ2File(path + "test.nbz2","w")
for line in lines:
  bz2_handler.write(line)
bz2_handler.close()

!wc -l {path}test.nbz2

lines = [b"This is the fifth line", b"This is the sixth line"]

import gzip
gzip_handler = gzip.open(path + "test.gz","wb")
for line in lines:
  gzip_handler.write(line)
gzip_handler.close()

!wc -l {path}test.gz

!gunzip -c {path}test.gz
 

lines = [b"This is the seventh line", b"This is the eighth line"]

import lzma
lzma_handler = lzma.open(path + "test.xz","wb")
for line in lines:
  lzma_handler.write(line)
lzma_handler.close()

!wc -l {path}test.xz
