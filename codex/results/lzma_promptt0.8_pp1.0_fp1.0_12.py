import lzma
# Test LZMADecompressor (requires Python 2.7 or 3.3)
print(lzma.LZMADecompressor().decompress(b'\x00\x00\x02\xffZLIB\x00\x00\x00\x00\x00\x00\x80\x00'))
# Output: b'1234567890'

import lzma
compressor = lzma.LZMACompressor()
compressor.compress(b'1234567890')
print(compressor.flush())

import lzma
LZMA_FORMAT_AUTO = 0
LZMA_FORMAT_XZ = 1
LZMA_FORMAT_ALONE = 2
LZMA_FORMAT_RAW = 4
LZMA_CHECK_NONE = 0
LZMA_CHECK_CRC32 = 1
LZMA_CHECK_CRC64 = 4
LZMA_CHECK_SHA256 = 10
compressor = lzma.LZMACompressor(format=LZMA_FORMAT_XZ, check=LZMA_CHECK
