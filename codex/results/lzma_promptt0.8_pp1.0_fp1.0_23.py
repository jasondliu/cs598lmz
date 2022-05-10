import lzma
# Test LZMADecompressor objects

def check_valid_data(data):
    raise NotImplementedError

p = lzma.LZMADecompressor()
assert p.unused_data == b""
assert p.eof is False
assert p.needs_input is True

d = p.decompress(b"a")
assert d == b"a"
assert p.unused_data == b""
assert p.eof is False
assert p.needs_input is True

d = p.decompress(b"a")
assert d == b""
assert p.unused_data == b""
assert p.eof is False
assert p.needs_input is True

d = p.decompress(b"bcdef", 2)
assert d == b"bc"
assert p.unused_data == b"def"
assert p.eof is False
assert p.needs_input is True

d = p.decompress(b"w")
assert d == b""
assert p.unused_data == b"defw"
assert p.e
