import lzma
lzma.decompress(open('test.xz', 'rb').read())

# 使用gzip
import gzip
f = gzip.open('test.txt.gz', 'r')
f.read()
f.close()

# 使用bz2
import bz2
f = bz2.BZ2File('test.txt.bz2', 'r')
f.read()
f.close()
