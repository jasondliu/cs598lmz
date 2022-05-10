import lzma
# Test LZMADecompressor.readinto() and LZMADecompressor.unused_data

s = b"This is a compressed string... "
d = zlib.compressobj()
compressed = d.compress(s)
compressed += d.flush()
assert len(s) > len(compressed)

# Decompress to a buffer
buf = compressed + b'1234'
d = lzma.LZMADecompressor()
b2 = bytearray(len(s))
n = d.readinto(b2)
b2 = bytes(b2)
b3 = d.unused_data
assert n == len(s)
assert b2 == s
assert b3 == b'1234'
# Test LZMADecompressor decompressing one by one

data = b"Hello world!"
data_enc = lzma.LZMAEncoder().compress(data)

dec = lzma.LZMADecompressor()

assert dec.decompress(data_enc[:6]) == b""
assert dec.dec
