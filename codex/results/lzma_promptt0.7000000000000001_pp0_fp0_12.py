import lzma
# Test LZMADecompressor
assert b"\x00"*lzma._BUFFER_SIZE in lzma.LZMADecompressor().decompress(b"x"*lzma._BUFFER_SIZE)
# Test BZ2Decompressor
assert b"\x00"*bz2._BUFFER_SIZE in bz2.BZ2Decompressor().decompress(b"x"*bz2._BUFFER_SIZE)
# Test ZlibDecompressor
assert b"\x00"*zlib._BUFFER_SIZE in zlib.decompress(b"x"*zlib._BUFFER_SIZE)
