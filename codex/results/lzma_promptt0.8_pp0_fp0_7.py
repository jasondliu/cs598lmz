import lzma
# Test LZMADecompressor
assert lzma.decompress(lzma.compress(b'12345678')) == b'12345678'


import bz2
# Test BZ2Compressor
assert bz2.decompress(bz2.compress(b'12345678')) == b'12345678'


import zlib
# Test ZlibCompressor
assert zlib.decompress(zlib.compress(b'12345678')) == b'12345678'
# zlib.tobytes(zlib.compress('12345678'))


import snappy
# Test SnappyCompressor
assert snappy.decompress(snappy.compress(b'12345678')) == b'12345678'


import brotli
# Test BrotliCompressor
assert brotli.decompress(brotli.compress(b'12345678')) == b'12345678'

import lz4
# Test LZ4Compressor
assert lz4.decompress(lz4.compress(b'
