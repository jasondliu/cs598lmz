import lzma
# Test LZMADecompressor

from lzma import LZMADecompressor
from lzma import FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE
from lzma import FILTER_LZMA1, FILTER_LZMA2
from lzma import CHECK_NONE, CHECK_CRC32, CHECK_CRC64, CHECK_SHA256

from io import BytesIO

# Test basic decompression

decomp = LZMADecompressor()
data = decomp.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04')
assert decomp.unused_data == b''
assert decomp.eof is True

# Test decompression with multiple calls to decompress()

decomp = LZMADecompressor()
data = decomp.decompress(b'\xfd
