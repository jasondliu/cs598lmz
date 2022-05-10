import bz2
# Test BZ2Decompressor
test_decompressor = BZ2Decompressor()
test_decompressor.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

import gzip
gz = gzip.open('data/file.txt.gz', 'rb')
gz_bytes = gz.read()
gz.close()
print(gz_bytes)

import zlib
compressor = zlib.compressobj(9, zlib.DEFLATED, zlib.MAX_WBITS | 16)
compressed = compressor.compress(b'witch which has which witches hand which')
compressed += compressor.flush()
print(compressed)

decompressor = zlib.decompressobj()
print(decompressor.decompress(compressed))

# import lzma
# compressor = lzma.LZMACompressor()
# print(compressor.compress(b'witch which has which witches hand which'))
