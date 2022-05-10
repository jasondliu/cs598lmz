import lzma
lzma.decompress(open('test.xz', 'rb').read())

# 使用gzip
import gzip
