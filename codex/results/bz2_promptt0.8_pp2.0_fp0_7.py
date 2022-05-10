import bz2
# Test BZ2Decompressor:
# - decompress some bytes
# - return unused_data
# - feed empty bytes
d = bz2.BZ2Decompressor()
assert d.decompress(b"BZh9") == b"foo"
assert d.unused_data == b"bar"
assert d.decompress(b"") == b""
assert d.unused_data == b""
# Test BZ2Decompressor on incomplete data:
# - bz2 frame ends with unexpected EOF, this should raise an EOFError
# - feed data only partially decompressed (notably some of the last CRC rest)
# - feed empty data
d = bz2.BZ2Decompressor()
assert d.decompress(b"BZh9fo") == b"foo"
try:
    d.decompress(b"BZh9")
except EOFError:
    pass
else:
    assert False, "expected EOFError"
d = bz2.BZ2Decompressor()
assert d.decompress(b"BZh9")
