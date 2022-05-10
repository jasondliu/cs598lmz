import lzma
# Test LZMADecompressor and LZMAEncoder
enc = lzma.LZMAEncoder()
out = enc.encode(b"foo")
out += enc.encode(b"bar")
codec = lzma.LZMADecompressor()
# Issue #27711: reset() shouldn't raise an error
codec.reset()
res = codec.decompress(b"")
res += codec.decompress(out)
assert res == b"foobar"
# Issue #27711: reset() shouldn't raise an error
codec.reset()
res += codec.decompress(b"")
assert res == b"foobar"
# Issue #27711: reset() shouldn't raise an error
codec.reset()
try:
    codec.decompress(b"\x00")
except Exception as e:
    assert isinstance(e, EOFError)
else:
    assert False
# Issue #27711: reset() shouldn't raise an error
codec.reset()
assert codec.decompress(b"") == b""

# Issue #27711:
