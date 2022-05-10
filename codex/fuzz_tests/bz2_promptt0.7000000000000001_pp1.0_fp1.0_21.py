import bz2
# Test BZ2Decompressor with multiple concatenated streams

data = bz2.BZ2Compressor().compress(b'foo')
data += bz2.BZ2Compressor().compress(b'bar')
data += bz2.BZ2Compressor().flush()

d = bz2.BZ2Decompressor()
assert d.decompress(data) == b'foobar'
assert d.unused_data == b''
assert d.eof == True

# Test BZ2Decompressor with non-concatenated streams

data1 = bz2.BZ2Compressor().compress(b'foo')
data2 = bz2.BZ2Compressor().compress(b'bar')
data2 += bz2.BZ2Compressor().flush()

d = bz2.BZ2Decompressor()
assert d.decompress(data1) == b''
assert d.unused_data == b''
assert d.eof == False
assert d.decompress(data2) == b'foobar'
assert
