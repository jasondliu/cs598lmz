from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2
# bz2.decompress(data)

# lzma
# lzma.decompress(data)

# zlib
# zlib.decompress(data)

print(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'.decode('latin-1'))
