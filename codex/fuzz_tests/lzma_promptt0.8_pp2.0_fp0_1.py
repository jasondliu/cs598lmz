import lzma
# Test LZMADecompressor class
d = lzma.LZMADecompressor()
d.decompress(b'lzma compressed data')
# More efficient to use one object per thread with LZMAFile
# with lzma.open('some-file.xz', 'rt') as f:
#     text = f.read()

# lzma.compress() and lzma.decompress() used for single blocks of data
binary_data = open('lorem.xz', 'rb').read()
uncompressed = lzma.decompress(binary_data)
# Does not handle headers, footers, or integrity checks contained in some .xz files
# bz2 - provides data compression using the bzip2 algorithm
import bz2
# Test BZ2Compressor class:
c = bz2.BZ2Compressor()
c.compress(b'data to compress')
c.flush()
# More efficient to use one object per thread with BZ2File
# with bz2.open('some-file.bz2', 'wt') as f:

