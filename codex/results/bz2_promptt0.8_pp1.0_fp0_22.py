import bz2
# Test BZ2Decompressor and BZ2Compressor classes

d = bz2.BZ2Decompressor()
assert d.unused_data == b''

c = bz2.BZ2Compressor()
assert c.flush(b'') == b''
assert c.flush(b"a") == b"BZ"
assert c.flush(b'') == b"h\x01\x31\x00\x00\x00\x01\x00"
assert c.flush(b'') == b''

data = b"hello world\n"
compressed_data = c.compress(data)
assert len(compressed_data) < len(data)
decompressed_data = bz2.decompress(compressed_data)
assert decompressed_data == data

# Test that we can do the same with an in-memory buffer
d = bz2.BZ2Decompressor()
o = d.decompress(bz2.compress(b"abc"))
assert o == b"abc"
o = d.decompress(b
