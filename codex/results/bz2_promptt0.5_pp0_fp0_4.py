import bz2
# Test BZ2Decompressor.__init__()

decomp = bz2.BZ2Decompressor()

try:
    decomp.decompress(b"")
except IOError as e:
    print(e)
# Test BZ2Decompressor.__init__() with a small buffer

decomp = bz2.BZ2Decompressor(1)

try:
    decomp.decompress(b"")
except IOError as e:
    print(e)
# Test BZ2Decompressor.__init__() with a large buffer

decomp = bz2.BZ2Decompressor(100)

try:
    decomp.decompress(b"")
except IOError as e:
    print(e)
# Test BZ2Decompressor.decompress()

decomp = bz2.BZ2Decompressor()

decomp.decompress(b"BZh91AY&SY")
decomp.decompress(b"A")

try:
    decomp.decompress(b"")
except IO
