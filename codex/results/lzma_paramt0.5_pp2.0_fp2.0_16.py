from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xff\xff')

# Issue #27240: The LZMADecompressor class now supports the
# decompress_from() method.
from io import BytesIO
compressor = LZMADecompressor()
compressor.decompress_from(BytesIO(b'\xff\xff'))

# Issue #27240: The LZMADecompressor class now supports the flush() method.
compressor = LZMADecompressor()
compressor.flush()

# Issue #27240: The LZMADecompressor class now supports the unused_data
# attribute.
compressor = LZMADecompressor()
compressor.decompress(b'\xff\xff')
assert compressor.unused_data == b''

# Issue #27240: The LZMADecompressor class now supports the
# decompress_from() method.
compressor = LZMADecompressor()
compressor.decompress_from(BytesIO(b'\xff\xff'))
assert compressor.unused
