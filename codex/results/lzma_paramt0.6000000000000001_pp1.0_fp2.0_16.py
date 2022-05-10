from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00')

# lzma.LZMADecompressor.flush()
# lzma.LZMADecompressor.decompress()
# lzma.LZMADecompressor.__init__()

# lzma.LZMADecompressor.eof
# lzma.LZMADecompressor.unused_data

# lzma.LZMADecompressor.__init__()
"""
Initialize a decompressor object.

The *format* parameter specifies which container format to assume for the input data; if it is omitted or ``None``, the decompressor will try to determine the container format automatically.

The *check* parameter specifies which integrity checks (if any) to verify when decompressing data. If it is omitted or ``None``, the decompressor will try to determine the integrity check used from the container format.

If ``format`` is not ``None``, it must be an integer in the range 0-3, or
