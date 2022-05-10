import bz2
# Test BZ2Decompressor and BZ2Compressor classes

d = bz2.BZ2Decompressor()
assert d.unused_data == b''

c = bz2.BZ2Compressor()
