from lzma import LZMADecompressor
LZMADecompressor.__doc__="""--lzma-decompressor
test_decompressor

XXX ToDo: test
"""

from zlib import (adler32, compress, compressobj, decompress,
    crc32, flush_libz_buffer, MAX_WBITS, DEFLATED,
    ZLIB_RUNTIME_VERSION, ZLIB_VERSION)
adler32.__doc__ = """adler32(string, value) -- Compute an Adler-32 checksum of string.

An optional starting value may be given in value.
The returned checksum is an integer."""
compressobj.__doc__ = """compressobj([level]) -- Return a compressor object.

Optional arg level is the compression level, in 1-9.
"""
decompress.__doc__ = """decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.

Optional arg wbits is the window buffer size.
Optional arg bufsize is the initial output buffer size.
"""
crc32.__doc__ = """crc32(string,[start]) -- Comp
